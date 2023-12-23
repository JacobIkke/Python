# MT3608 calculations.
import math

# Calculates Vout
vin = 5.0  # replace with your actual value for Vin
r1 = 10000.0  # replace with your actual value for R1 in Ohm's
r2 = 2150.0  # replace with your actual value for R2 in Ohm's

def calculate_vout(vin, r1, r2):
    vout = vin * (1 + r1 / r2)
    return vout

volt_out = calculate_vout(vin, r1, r2)
print(f"Vout: {volt_out} Volts")


# Calculates Inductor Current Ripple, delta (ΔIL) 
output_voltage = 15.0  # replace with your actual value for output voltage (Vout) in Volts
duty_cycle = 0.5  # replace with your actual value for duty cycle (D)
switching_frequency = 1500000  # replace with your actual value for switching frequency (fs) in Hertz
inductor_value = 0.000220  # replace with your actual value for inductor value (L) in Henrys

def calculate_inductor_current_ripple(output_voltage, duty_cycle, switching_frequency, inductor_value):
    delta_il = (output_voltage * (1 - duty_cycle)) / (switching_frequency * inductor_value)
    return delta_il

il = calculate_inductor_current_ripple(output_voltage, duty_cycle, switching_frequency, inductor_value)
print(f"Inductor Current Ripple: {il} Amperes")


#  Calculates Output Ripple Voltage
delta_il = 0.045  # replace with your actual value for inductor current ripple (ΔIL)
duty_cycle = 0.5  # replace with your actual value for duty cycle (D)
inductor_value = 0.000220  # replace with your actual value for inductor value (L) in Henrys
output_capacitor_value = 0.000047 # replace with your actual value for output capacitor value (Cout) in Farads

def calculate_output_ripple_voltage(delta_il, duty_cycle, inductor_value, output_capacitor_value):
    delta_vout = (delta_il * duty_cycle * (1 - duty_cycle) * inductor_value) / output_capacitor_value
    return delta_vout

Ripple_Vout = calculate_output_ripple_voltage(delta_il, duty_cycle, inductor_value, output_capacitor_value)
print(f"Output Ripple Voltage: {Ripple_Vout} Volts")


# Calculates Diode RMS current
peak_current = 2.0  # replace with your actual value for peak current
average_current = 1.5  # replace with your actual value for average current

def calculate_diode_rms_current(peak_current, average_current):
    diode_rms_current = math.sqrt(peak_current**2 + average_current**2)
    return diode_rms_current

rms_current = calculate_diode_rms_current(peak_current, average_current)
print(f"Diode RMS Current: {rms_current} Amperes")
