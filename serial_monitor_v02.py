# 19-05-2023
# PeetHobby @Peetgaming
# Python Serial Monitor with tkinter V0.2

import tkinter as tk
from tkinter import scrolledtext
import serial.tools.list_ports

ser = None
baud_rate = None

def connect_serial():
    global ser
    port = port_var.get()
    baud_rate = baud_rate_var.get()
    try:
        ser = serial.Serial(port, baud_rate)
        textbox.insert(tk.END, f"Connected to {port} at {baud_rate} baud\n")
        textbox.after(100, read_serial)  # Start reading data after 100ms
    except serial.SerialException as e:
        textbox.insert(tk.END, f"Failed to connect to {port}: {str(e)}\n")

def disconnect_serial():
    global ser
    if ser is not None and ser.is_open:
        ser.close()
        textbox.insert(tk.END, "Serial port disconnected\n")

def read_serial():
    global ser
    try:
        if ser is not None and ser.is_open and ser.in_waiting > 0:
            received_data = ser.readline().decode().strip()
            textbox.insert(tk.END, f"Received: {received_data}\n")
            textbox.see(tk.END)  # Scroll to the end of the text
    except serial.SerialException as e:
        textbox.insert(tk.END, f"Error reading from serial port: {str(e)}\n")
    textbox.after(500, read_serial)  # Schedule the next read after 100ms

# Create the main Tkinter window
window = tk.Tk()
window.title("Serial Monitor V01")

# COM ports Selection
port_frame = tk.Frame(window)
port_frame.pack(padx=5, pady=5)

port_label = tk.Label(port_frame, text="Port:")
port_label.pack(side=tk.LEFT)

available_ports = [port.device for port in serial.tools.list_ports.comports()]
port_var = tk.StringVar(window)
port_var.set(available_ports[0] if available_ports else "")
port_dropdown = tk.OptionMenu(port_frame, port_var, *available_ports)
port_dropdown.pack(side=tk.LEFT)

# Baud rate selection
baud_rate_frame = tk.Frame(window)
baud_rate_frame.pack(padx=5, pady=5)

baud_rate_label = tk.Label(baud_rate_frame, text="Baud Rate:")
baud_rate_label.pack(side=tk.LEFT)

baud_rate_var = tk.StringVar(window)
baud_rate_var.set("9600")
baud_rate_dropdown = tk.OptionMenu(baud_rate_frame, baud_rate_var, "9600", "19200", "38400", "115200")
baud_rate_dropdown.pack(side=tk.LEFT)

# textboxes
textbox = scrolledtext.ScrolledText(window, height=20, width=50)
textbox.pack()

# buttons
connect_button = tk.Button(window, text="Connect", command=connect_serial)
connect_button.pack(side=tk.LEFT, padx=5, pady=5)

disconnect_button = tk.Button(window, text="Disconnect", command=disconnect_serial)
disconnect_button.pack(side=tk.LEFT, padx=5, pady=5)

window.mainloop()

