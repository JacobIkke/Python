# 6 bits: 63
# 7 bits: 127
# 8 bits: 255
# 9 bits: 511
# 10 bits: 1023
# 11 bits: 2047
# 12 bits: 4095
# 13 bits: 8191
# 14 bits: 16383
# 15 bits: 32767
# 16 bits: 65535
# 32 bits: 4294967295

# The Timer Inputs, adjust those values based on your requirements.
timer_clock_frequency = 170000000  # Timer clock in hz, in most cases; timers are coupled to APB1, APB2, etc.
timer_prescaler = 65535 # Max: 16-bit for 16bit timers, and 32bit for 32bit timers. 
timer_period = 65535 # Max: 16-bit for 16bit timers, and 32bit for 32bit timers. 

# The Calculation
def calculate_timer_frequency(clock_frequency, prescaler, period):
    timer_frequency = clock_frequency / ((prescaler + 1) * (period + 1))
    return timer_frequency

# The Output
timer_frequency = round(calculate_timer_frequency(timer_clock_frequency, timer_prescaler, timer_period), 5)
print(f"Timer Frequency in Hz = {timer_frequency} Hz")





