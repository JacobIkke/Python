#
# Sine Wave Lock Up Table Generator v1
# 04-13-2023 16:56
# PeetHobby @PeetGaming
#

import math

amplitude = 65535  # unsigned integer. example: uint16 65535
size_array = 256 # size of the array
row_size = 32 # how many numbers per row

def gen_sine_table(amplitude, size_array):
    wave_table = [] 
    for i in range(size_array):
        value = int(amplitude * math.sin(i * 2 * math.pi / size_array) + amplitude) 
        value_hex = hex(value)[2:].upper()  
        wave_table.append(value_hex) 
    return wave_table

# generate the table
sine_table = gen_sine_table((amplitude / 2)+1, size_array)

# print the C array sin wave lookup table
print("const uint16_t sine_table[] = {", end="")
for i in range(0, len(sine_table), row_size):
    row = ", ".join([f"0x{x}" for x in sine_table[i:i+row_size]])
    print("  " + row + ",")
print("};")





