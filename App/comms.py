import time
import meshtastic
import meshtastic.serial_interface
import serial.tools.list_ports
from pubsub import pub
from worker import Worker
from PySide6.QtCore import (
        QRunnable,
        QThreadPool,
        QTimer,
        Slot,
        QObject,
        Signal,
    )
class MeshGateway(QObject):
    connection_changed = Signal(bool)
    def __init__(self):
        super().__init__()
        self.interface = None
        self.is_connecting = False
        self.threadpool = QThreadPool()  # Radio handles its own threads
        
        pub.subscribe(self.onDisconnect, "meshtastic.connection.lost")
        pub.subscribe(self.onConnection, "meshtastic.connection.established")

    def connect(self):
       #start connection with our gateway 
        if self.is_connecting:
            return
        self.is_connecting = True
             #threads
        worker = Worker(self.connection_task)
        self.threadpool.start(worker)

    def connection_task(self):
        #trying to connect to the gateway device and handles if it fails
        # This is why we thread
        while self.is_connecting:
            try:
                # Try to initialize the serial interface
                new_interface = meshtastic.serial_interface.SerialInterface()
                
                if new_interface.devPath:
                    self.interface = new_interface
                    self.is_connecting = False  # UNLOCKS SENDING LOGIC
                    self.connection_changed.emit(True)
                    print(f"Connected to {self.interface.devPath}")
                    break 
                else:
                    new_interface.close()
                    time.sleep(2)
            except Exception as e:
                time.sleep(2)
        # while self.is_connecting:
        #     try:
        #         if not self.is_connecting:
        #             break
                
        #         self.interface = meshtastic.serial_interface.SerialInterface()
        #         print(self.interface)
        #         if self.interface.devPath:
        #             break
        #         else:
        #             self.interface.close()
        #             self.interface = None
        #     except Exception as e:
        #         # print("Error device not connected\n")
        #         if not self.is_connecting:
        #             break
        #         # print(f"trying again in 3 seconds {e}")
        #         time.sleep(2)

  # comms.py

    def onConnection(self, interface=None, **kwargs):
        if self.interface is None and interface:
             self.interface = interface
    
        self.is_connecting = False
        self.connection_changed.emit(True)
    def onDisconnect(self, interface=None, **kwargs):
        if not self.is_connecting:
                    print("Connection lost, attempting to reconnect...")
                    self.interface = None
                    self.connection_changed.emit(False)
                    self.connect()
        
        #if this fails we know whyyyyyyyyyyy
    def send_message(self, TeamAPID, TeamBPID,TeamCPID,TeamDPID,urgency="ffffff" ):
        #call message task and start thread
        worker = Worker(self.send_message_task, TeamAPID, TeamBPID,TeamCPID,TeamDPID,urgency)
        self.threadpool.start(worker)

    def send_message_task(self, TeamAPID, TeamBPID,TeamCPID,TeamDPID,urgency="ffffff"):
        #send the message to the teams should be reusable with u and manual modes
        
        print("sending\n")
        messager = "red team head to arena\n"
        messageb = "blue team head to arena\n"        
        formatted =  f"{TeamAPID}|{urgency}|{messager}{TeamBPID}|{urgency}|{messager}{TeamCPID}|{urgency}|{messageb}{TeamDPID}|{urgency}|{messageb}"
        sent = False
        while not sent:
   # c         while self.interface is None or self.is_connecting:
            while self.is_connecting or self.interface is None:
                # print(f"interface == {self.interface}\n")
                # print(f"is connecting == {self.is_connecting}\n")
                # print("sending sent waiting for connection to device")
                time.sleep(2)
            try:
                self.interface.sendText(formatted)
                # print(f"sending mesages \n {formatted}")
                sent = True
            except Exception as e:
                # print(f" sending failed due to {e}\n device disconnected \n sending paused to recconnection")
                sent = False
                time.sleep(2)
    def send_message_single(self, TeamFPID,urgency="ffffff"):
        worker = Worker(self.send_message_single_task,TeamFPID,urgency)
        self.threadpool.start(worker)
    def send_message_single_task(self, TeamFPID,Urgency):
        message = "head to arena now\n"
        formatted = f"{TeamFPID}|{Urgency}|{message}"
        sent = False
        while not sent:
            while self.interface is None or self.is_connecting:
                print("sending sent waiting for connection to device")
                time.sleep(2)
            try:
                self.interface.sendText(formatted)
                print(f"sending mesages \n {formatted}")
                sent = True
            except Exception as e:
                print(f" sending failed due to {e}\n device disconnected \n sending paused to recconnection")
                sent = False
                time.sleep(2)
        
    def provision(self, channel_name = "robotics", channel_key="aqYv"):
        while self.interface is None or self.is_connecting:
            time.sleep(2)
        try:
            pid = self.interface.getShortName()
            node = self.interface.getNode('local')
            node.setChannel(
                name = channel_name,
                key = channel_key,
                index = 0
            )
            node.writeConfig()
            return pid
            
    def exit(self):
        #close connection between the device and also shutdown the threadpool
        self.is_connecting = False
        pub.unsubscribe(self.onDisconnect, "meshtastic.connection.lost")
        pub.unsubscribe(self.onConnect, "mestastic.connection.established")
        if self.interface:
            try:
                 self.interface.close()
            except:
                pass
            
        print(f"Gateway connection terminated ready to shutdown")
        self.threadpool.clear()
      
def get_pid():
    temp_interface = None
    try:
        temp_interface = meshtastic.serial_interface.SerialInterface()
        if temp_interface.devPath:
            pid = temp_interface.getShortName()
            print(pid)
            return(print("{pid}"))
        else:
            print ("no pid")
            return None
    except Exception as e:
        print(f"pid check failed: {e}")
        return None
    finally:
        if temp_interface:
            try:
                temp_interface.close()
            except:
                pass
