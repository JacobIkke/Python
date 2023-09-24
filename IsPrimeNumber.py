# This is micro python port of code form Youtuber Ralph S Bacon, give his channel some love!  
# Simple prime number benchmark.
#
# Some test scores:
# Pico Python 125Mhz = 36s (Thonny)
# Pico Python 256Mhz = 18s (Thonny)
#
# Other platforms/languages test scores:
# Pico C sdk 125Mhz  = 996 ms (vscode)
# Pico C sdk 256Mhz  = 486 ms (vscode)
# Arduino 16Mhz = 120s (Arduino software)
# LGT8F328p 32Mhz 59s (Arduino software)
# STM32F103 72Mhz = 3s (Arduino software, I didn't run this myself!)
# STM32H750 480Mhz = 186 ms (stm32cube)
#
# P.S.
# I keep the code simular across platforms and languages as much as possible. 

import math
import time

machine.freq(125000000)
print("CPU Speed: ", int(machine.freq() / 1000000), "MHz \n")

def find_primes(max_primes):
    i = 2
    found = 0
    last_prime = 0
    last_found = 0
    start = time.time()

    while True:
        prime = is_prime(i)

        if prime:
            last_prime = i
            found += 1

            #if found % 10 == 0:
                #print(f"{found}: ", end='')

        elapsed_seconds = int(time.time() - start)

        if found >= max_primes:
            print("\nFound", found, "primes in", elapsed_seconds, "seconds")
            print("Highest prime found was:", last_prime, "\n")
            time.sleep(10)

            i = 2
            found = 0
            last_prime = 0
            print("Prime calculation starting (again)")
            start = time.time()
        else:
            i += 1
            
def is_prime(num):
    if num <= 1:
        return False

    upper = int(math.sqrt(num))

    for cnum in range(2, upper + 1):
        mod = num % cnum

        if mod == 0:
            return False

    return True


# Usage example:
max_primes_to_find = 10000
find_primes(max_primes_to_find)
