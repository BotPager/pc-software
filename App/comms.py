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
                time.sleep(2)

    #pub sub connection event
    def onConnection(self, interface, topic=pub.AUTO_TOPIC):
        print("good")
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
    def send_message(self, TeamAPID, TeamBPID,TeamCPID,TeamDPID):
        #call message task and start thread
        worker = Worker(self.send_message_task, TeamAPID, TeamBPID,TeamCPID,TeamDPID)
        self.threadpool.start(worker)

    def send_message_task(self, TeamAPID, TeamBPID,TeamCPID,TeamDPID):
        #send the message to the teams should be reusable with automatic and manual modes
        print("sending")
        message = "|go to pit"
        messageTeamA = TeamAPID + message
        messageTeamB = TeamBPID + message
        messageTeamC = TeamCPID + message
        messageTeamD = TeamDPID + message
        
        sent = False
        while not sent:
            while self.interface is None or self.is_connecting:
                print("sending sent waiting for connection to device")
                time.sleep(5)
            try:
                self.interface.sendText(messageTeamA)
                print(f"team A {messageTeamA}")
                time.sleep(5)
                self.interface.sendText(messageTeamB)
                print(f"team B {messageTeamB}")
                time.sleep(5)
                self.interface.sendText(messageTeamC)
                print(f"team C {messageTeamC}")
                time.sleep(5)
                self.interface.sendText(messageTeamD)
                print(f"team D {messageTeamD}")
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

def get_all_pids():
    all_pids = []
    
    # Get all serial ports
    ports = serial.tools.list_ports.comports()
    
    for port in ports:
        temp_interface = None
        try:
            # Try to connect to this specific port
            print(f"Checking port: {port.device}")
            temp_interface = meshtastic.serial_interface.SerialInterface(port.device)
            
            if temp_interface.devPath:
                # Wait a moment for connection to stabilize
                time.sleep(1)
                
                # Get the PID (short name)
                pid = temp_interface.getShortName()
                
                if pid:
                    all_pids.append({
                        'port': port.device,
                        'pid': pid,
                        'description': port.description
                    })
                    print(f"Found device on {port.device} with PID: {pid}")
                else:
                    print(f"No PID returned from {port.device}")
        
        except Exception as e:
            # Not a meshtastic device or connection failed
            print(f"Could not connect to {port.device}: {e}")
        
        finally:
            # Always close the connection to this device
            if temp_interface:
                try:
                    temp_interface.close()
                except:
                    pass
    
    return all_pids

def get_all_pids_simple():
    """
    Simplified version - returns just the list of PIDs as strings.
    """
    devices = get_all_pids()
    return [device['pid'] for device in devices]

# def set_settings():
#     temp_interface = None
#     try:
#         temp_interface = meshtastic.serial_interfaace.SerialInterface()
#         if temp_interface.devPath:
#         else
#     except Exception as e:
#         print(f"error: {e}")
#         return None
#     finally
#         if temp_interface:
#             try:
#                 temp_interface.close()
#             except:
#                 pass
