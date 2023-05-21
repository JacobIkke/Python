# 20-05-2023
# PeetHobby @Peetgaming
# Python Serial Monitor with tkinter V0.3
import tkinter as tk
from tkinter import scrolledtext
import serial.tools.list_ports

ser = None
baud_rate = None
after_id = None

def connect_serial():
    textbox.delete("1.0", tk.END)
    global ser
    global after_id
    port = port_var.get()
    baud_rate = baud_rate_var.get()
    try:
        ser = serial.Serial(port, baud_rate)
        textbox.insert(tk.END, f"Connected to {port} at {baud_rate} baud\n")
        after_id = textbox.after(100, read_serial)  # Start reading data after 100ms
    except serial.SerialException as e:
        textbox.insert(tk.END, f"Failed to connect to {port}: {str(e)}\n")

def disconnect_serial():
    global ser
    global after_id
    if ser is not None and ser.is_open:
        ser.close()
        textbox.after_cancel(after_id)  # Cancel the recurring calls
        after_id = None
        textbox.insert(tk.END, "Serial port disconnected\n")
        ser = None
        baud_rate = None

def read_serial():
    global ser
    global after_id
    try:
        if ser is not None and ser.is_open and ser.in_waiting > 0:
            received_data = ser.readline().decode().strip()
            textbox.insert(tk.END, f"Received: {received_data}\n")
            textbox.see(tk.END)  # Scroll to the end of the text
    except serial.SerialException as e:
        textbox.insert(tk.END, f"Error reading from serial port: {str(e)}\n")
    after_id = textbox.after(100, read_serial)  # Schedule the next read after 100ms
    
def send_serial():
    # Function to handle button click event
    input_text = input_entry.get()  # Get the text entered in the Entry widget
    print("Entered text:", input_text) # Sehll output
    textbox.insert(tk.END, f"Sending: {input_text}\n", "sending_tag")
    textbox.tag_config("sending_tag", foreground="blue")
    try:
        ser.write(input_text.encode())  # Convert the string to bytes and send it over the serial connection
        print("Data sent successfully!")
    except serial.SerialException as e:
        print(f"Serial port error: {str(e)}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Create the main Tkinter window
window = tk.Tk()
window.title("Serial Monitor V0.3")

# Set the window icon
#window.iconbitmap("icon_round1.ico") # Optional icon.

# COM ports Selection
top_frame = tk.Frame(window)
top_frame.pack(padx=5, pady=5)

port_label = tk.Label(top_frame, text="Port:")
port_label.pack(side=tk.LEFT)

available_ports = [port.device for port in serial.tools.list_ports.comports()]
port_var = tk.StringVar(window)
port_var.set(available_ports[0] if available_ports else "")
port_dropdown = tk.OptionMenu(top_frame, port_var, *available_ports)
port_dropdown.pack(side=tk.LEFT)

# Baud rate selection
baud_rate_frame = top_frame #tk.Frame(window)
baud_rate_frame.pack(padx=5, pady=5)

baud_rate_label = tk.Label(baud_rate_frame, text="Baud Rate:")
baud_rate_label.pack(side=tk.LEFT)

baud_rate_var = tk.StringVar(window)
baud_rate_var.set("115200")
baud_rate_dropdown = tk.OptionMenu(baud_rate_frame, baud_rate_var, "300", "600", "1200", "2400", "4800", "9600", "19200", "38400", "115200", "230400", "500000", "1000000")
baud_rate_dropdown.pack(side=tk.LEFT)

# Buttons top_frame, Connect button
connect_button = tk.Button(top_frame, text="Connect", command=connect_serial)
connect_button.pack(side=tk.LEFT, padx=5, pady=5)
# Disconnect button
disconnect_button = tk.Button(top_frame, text="Disconnect", command=disconnect_serial)
disconnect_button.pack(side=tk.LEFT, padx=5, pady=5)

# Textbox
textbox = scrolledtext.ScrolledText(window, height=20, width=60)
textbox.pack(padx=10, pady=5)

# One-line input textbox
input_frame = tk.Frame(window)
input_frame.pack(padx=5, pady=5)

input_label = tk.Label(input_frame, text="Input:")
input_label.pack(side=tk.LEFT)

input_entry = tk.Entry(input_frame, width=60)  # Adjust the width as needed
input_entry.pack(side=tk.LEFT)

# Buttons input_frame
send_button = tk.Button(input_frame, text="Send", command=send_serial, width=7, height=1)
send_button.pack(side=tk.LEFT, padx=5, pady=5)

window.mainloop()
