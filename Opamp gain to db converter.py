import math

# 1. Gain to db
def gain_to_decibel(gain):
    # Check if gain is non-positive
    if gain <= 0:
        raise ValueError("Gain must be positive.")

    # Calculate decibel level
    dB = 20 * math.log10(gain)
    return dB

# Example usage
gain = 30.0  # replace with your actual gain value

result_dB = gain_to_decibel(gain)
print(f"The decibel level of {gain} voltage gain = {result_dB} dB")

# 2. db to gain
def decibel_to_gain(dB):
    # Calculate gain
    gain = 10 ** (dB / 20)
    return gain

# Example usage
dB = 20.0  # replace with your actual dB value

result_gain = decibel_to_gain(dB)
print(f"The gain of {dB} db = {result_gain}")

# 3. Vin and Vout to db
def calculate_decibel(Vin, Vout):
    # Check if V1 or V2 is non-positive
    if Vin <= 0 or Vout <= 0:
        raise ValueError("Voltage values must be positive.")

    # Calculate decibel level
    dB = 20 * math.log10(Vout / Vin)
    return dB

# Example usage
Vin = 1.0   # replace with your Vin voltage
Vout = 10.0  # replace with your Vout voltage

result_dB = calculate_decibel(Vin, Vout)
print(f"The decibel level of Vin {Vin}V and Vout {Vout}V = {result_dB} dB")