import time
import meshtastic
import meshtastic.serial_interface
from pubsub import pub
from worker import Worker
from PySide6.QtCore import (
        QRunnable,
        QThreadPool,
        QTimer,
        Slot
    )
class MeshGateway:
    def __init__(self):
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
                print("connecting")
                if not self.is_connecting:
                    break
                
                self.interface = meshtastic.serial_interface.SerialInterface()
                print(self.interface)
                if self.interface.devPath:
                    break
                else:
                    self.interface.close()
                    self.interface = None
            except Exception as e:
                print("Error device not connected\n")
                if not self.is_connecting:
                    break
                print(f"trying again in 3 seconds {e}")
                time.sleep(3)

    #pub sub connection event
    def onConnection(self, interface, topic=pub.AUTO_TOPIC):
        print("connected")
        self.is_connecting = False
    #pubsub discconnect event 
    def onDisconnect(self, interface, topic=pub.AUTO_TOPIC):
        print("disconnection occurred please recconnect")
        self.is_connecting = False
        if self.interface:
            try:
                self.interface.close()
            except:
                pass
            self.interface = None
        
        # Trigger reconnection thread
        self.connect()
#if this fails we know whyyyyyyyyyyy
    def send_message(self, TeamAPID, TeamBPid):
        #call message task and start thread
        worker = Worker(self.send_message_task, TeamAPID, TeamBPID)
        self.threadpool.start(worker)

    def send_message_task(self, TeamAPID, TeamBPID):
        #send the message to the teams should be reusable with automatic and manual modes
        print("sending")
        message = "|go to pit"
        messageTeamA = TeamAPID + message
        messageTeamB = TeamBPID + message
        
        sent = False
        while not sent:
            while self.interface is None or self.is_connecting:
                print("sending sent waiting for connection to device")
                time.sleep(5)
            try:
                self.interface.sendText(messageTeamA)
                time.sleep(5)
                self.interface.sendText(messageTeamB)
                sent = True
            except Exception as e:
                print(f" sending failed due to {e}\n device disconnected \n sending paused to recconnection")
                sent = False
                time.sleep(2)
    def exit(self):
        #close connection between the device and also shutdown the threadpool
        self.is_connecting = False
        if self.interface:
            try:
                 self.interface.close()
            except:
                pass
            
        print(f"Gateway connection terminated ready to shutdown")
        self.threadpool.clear()
      
