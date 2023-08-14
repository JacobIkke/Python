# Simple STM32 Timer calculator V1
# This formule comes out of the AN4013 Application note: STM32 cross-series timer overview

def calculate_timer_frequency(clock_frequency, prescaler, autoreload):
    RCR = 0 # Replace with your RCR if needed
    timer_frequency = clock_frequency / ((prescaler + 1) * (autoreload + 1) * (RCR + 1))
    return timer_frequency

# Replace these values with your actual values
clock_frequency = 72000000  	# Replace with your clock frequency in Hz
prescaler = 1            		# Replace with your prescaler value
autoreload = 65535            		# Replace with your autoreload value 

# Calculate the timer frequency using the function
f_tim = calculate_timer_frequency(clock_frequency, prescaler, autoreload)
print("Timer Frequency:", f_tim, "Hz")


