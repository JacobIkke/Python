# This code converts 8 binary bytes into a hexadecimal array.
# Simply draw something using 1s and 0s and execute the script.
# No further explanation is necessary I think. Enjoy! :D

# 8x8 field (D as example)
b1 = 0b11111000
b2 = 0b10000100
b3 = 0b10000010
b4 = 0b10000010
b5 = 0b10000010
b6 = 0b10000100
b7 = 0b11111000
b8 = 0b00000000


# print the font out as HEX with array brackets
print("{",format(b1, '#04x'),", ",
          format(b2, '#04x'),", ",
          format(b3, '#04x'),", ",
          format(b4, '#04x'),", ",
          format(b5, '#04x'),", ",
          format(b6, '#04x'),", ",
          format(b7, '#04x'),", ",
          format(b8, '#04x'), "}", sep='')
