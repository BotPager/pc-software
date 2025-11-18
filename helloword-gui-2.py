import tkinter as tk
import serial
import threading
import time

# --- Serial Setup ---
try:
    ser = serial.Serial("COM5", 9600, timeout=1)
    time.sleep(2)  # wait for Arduino reset
except serial.SerialException as e:
    ser = None
    print(f"Error opening serial port: {e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Serial Chat")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# --- Text Display Area ---
text_display = tk.Text(frame, height=15, width=50, state="disabled", wrap="word")
text_display.pack(pady=10)

# --- Entry & Send Button ---
entry = tk.Entry(frame, width=40, font=("Arial", 12))
entry.pack(side="left", padx=(0, 10))

def send_message():
    msg = entry.get().strip()
    if msg and ser and ser.is_open:
        ser.write((msg + "\n").encode())
        add_text(f"PC → {msg}\n", "green")
        entry.delete(0, tk.END)
    else:
        add_text("Serial port not open or empty message.\n", "red")

send_button = tk.Button(frame, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(side="left")

# --- Status Display ---
status_label = tk.Label(root, text="Connected" if ser else "Serial not open", fg="green" if ser else "red")
status_label.pack(pady=(5, 0))

# --- Text Utility ---
def add_text(text, color="black"):
    text_display.config(state="normal")
    text_display.insert(tk.END, text)
    text_display.tag_add(color, "end-1l linestart", "end-1l lineend")
    text_display.tag_config(color, foreground=color)
    text_display.config(state="disabled")
    text_display.see(tk.END)

# --- Thread to Continuously Read Serial ---
def read_serial():
    while ser and ser.is_open:
        try:
            line = ser.readline().decode(errors="ignore").strip()
            if line:
                root.after(0, lambda: add_text(f"Heltec → {line}\n", "blue"))
        except Exception as e:
            print(f"Serial read error: {e}")
            break

if ser:
    threading.Thread(target=read_serial, daemon=True).start()

# --- On Close ---
def on_close():
    if ser and ser.is_open:
        ser.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
