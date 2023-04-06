# Simple tool/code to calculate/simulate NTC thermistor and ADC calculations
# PeetHobby @PeetGaming
######################## Steinhart-Hart equation ##########################
import math
# NTC thermistor parameters
r0 = 10000    # The Resistance at reference temperature (25°C)
t0 = 25       # Reference temperature in Celsius 
beta = 3950   # Coefficient of the NTC in Kohm

def ntc_resistance(t):
    # calculate resistance of NTC thermistor at given temperature using Steinhart-Hart equation
    inv_t = 1 / (t + 273.15)   # convert to Kelvin
    inv_t0 = 1 / (t0 + 273.15)
    r = r0 * math.exp(beta * (inv_t - inv_t0))
    return r

# Give up temperature
ambient_temp = 10 # in Celsius 
print("Resistance for", str(ambiant_temp), "degree Celsius is: ", round(ntc_resistance(ambiant_temp)), "Ohm")
print()

#################### ADC calculations ##################################
# NTC thermistor and ADC parameters
BETA = 3950 # Coefficent of the NTC at 25°C in Kohm
R25 = 10000 # Resistor of the voltage divider with the NTC in Ohm
Vref = 5 # Vref in volts
Vin = 5 # Vin, power supply of the NTC
adc_val = 512  #10K NTC plus 10K resistor give 512(10b ADC) by 25°C. or 2048(12bit ADC) = 25°C

Vout = adc_val * (Vref / 1024.0)  # 1024 value is for the 10bit ADC, change that to 4096 for 12bit
RT   = 10000 / (Vin / Vout - 1.0) #10K is the value of the NTC
T = (1 / (1/298.16 + 1/BETA * math.log(RT/R25 ))) - 273.15

print("ADC Results : ", adc_val)
print("ADC to volt : ", round(Vout,2), "V")
print("Resistance  : ", round(RT), "Ohm")
print("Temperature : ", round(T, 2), "Celsius")
