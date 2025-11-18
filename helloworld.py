import serial
import time
ser = serial.Serial("COM5", 9600, timeout=1,
    dsrdtr=False, 
    rtscts=False   ) #arduino sketch on mcu uses 9600 baud.

time.sleep(2)
data_send = b"Hello\n"
try:
    ser.write(data_send)
    print(f"Sent: {data_send.decode().strip()}")
except serial.SerialException as e:
    print(f"Serial port error: {e}")
except Exception as e:
    print(f"unkown error occur: {e}")
finally:
    ser.close()