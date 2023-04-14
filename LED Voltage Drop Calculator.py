#
# LED Voltage Drop Calculator
# 04-14-2023 10:56
# PeetHobby @PeetGaming
#

# Inputs
led_voltage_in = float(input("Enter the LED voltage (in volts): "))
num_leds = int(input("Enter the number of LEDs in series: "))
supply_voltage = float(input("Enter the power supply voltage (in volts): "))
led_current = float(input("Enter the desired LED current (in milliamps): "))

# Calculations
led_voltage = num_leds * led_voltage_in
resistor_value = (supply_voltage - led_voltage) / (led_current / 1000) # Drop resistor vales
resistor_power = (supply_voltage - led_voltage) * (led_current / 1000) # Power disipation in resistor
led_power = led_voltage * (led_current / 1000) # Power consumption of the led

# Results
print("")
#print(f"For a {color} LED with a {supply_voltage}V power supply and {led_current}mA current, use a {round(resistor_value)} ohm resistor.")
print(f"For {num_leds} x {led_voltage_in}V LED(s) with a {supply_voltage}V power supply and the desired {led_current}mA current, you need to use a {round(resistor_value)} ohm resistor.")
print(f"The resistor will dissipate {round(resistor_power, 3)} mW of power.")
print(f"The voltage drop across the resistor will be {round(supply_voltage - led_voltage, 2)}V.")
print(f"The {num_leds} x LED(s) will consume a total of {round(led_power, 3)} mW of power.")