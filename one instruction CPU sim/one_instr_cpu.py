# Simple one instruction CPU simulator
# I use NAND, NAND is an universal gate, that means you can make any other logic gate with the NAND gate.
# Please read the  manual how to use the instructions, and be free to add more instruction. 
# The CPU runs a programs for the RAM, load the program first into RAM before it execute the program. 

class ONE_INSTRUCTION_CPU:
    def __init__(self):
        self.registers = [0] * 8 	# We decalre the 8 Registers
        self.RAM = [0] * 256 		# 256 Bytes of RAM
        self.pc = 0					# Program counter
        self.running = False		

    def run(self):
        self.running = True
        while self.running:
            opcode = self.RAM[self.pc]					# Get opcode
            operand1 = self.RAM[self.pc + 1]			# Get Oprand1
            operand2 = self.RAM[self.pc + 2]			# Get Oprand2
            self.pc += 3								# Increase program counter
            self.exec_instr(opcode, operand1, operand2)	# Call the execute function
            
    # Instruction Decode and Execute
    def exec_instr(self, opcode, operand1, operand2):
        if opcode == 0: 
            self.registers[operand1] = self.registers[operand2]  # Move
        elif opcode == 1:
            self.registers[operand1] = self.nand(self.registers[operand1], self.registers[operand2]) # NAND
        elif opcode == 2:
            self.registers[operand1] += operand2	# Add
        elif opcode == 3:
            self.registers[operand1] -= operand2 	# Subtract
        elif opcode == 4:
            self.registers[operand1] *= operand2	# Multply
        elif opcode == 5:
            self.registers[operand1] //= operand2	# Divide
        elif opcode == 6:
            self.registers[operand1] %= operand2	# Remainder 
        elif opcode == 7:
            self.running = False					# Halt
            
    # The one instruction that make all othere instructions
    def nand(self, a, b):
        return ~(a & b)
    
    # Program loader, load program into the RAM.
    def load_program(self, program):
        for i, instruction in enumerate(program):
            self.RAM[i * 3] = instruction[0]
            self.RAM[i * 3 + 1] = instruction[1]
            self.RAM[i * 3 + 2] = instruction[2]
            
    def reset_cpu(self):
        self.registers = [0] * 8 	
        self.RAM = [0] * 256
        self.pc = 0 
        
# Great new CPU instance            
cpu = ONE_INSTRUCTION_CPU()

# The program you like to run
program = [
    (0, 0, 1),   # Move the value of register 1 to register 0
    (1, 2, 3),   # Compute the NAND of registers 2 and 3, and store the result in register 1
    (2, 4, 5),   # Add the value 5 to register 4
    (3, 6, 7),   # Subtract the value 7 from register 6
    (4, 0, 4),   # Multiply the value in register 0 by the value in register 4, and store the result in register 0
    (5, 0, 3),   # Divide the value in register 0 by the value in register 3, rounding down to the nearest integer, and store the result in register 0
    (6, 0, 2),   # Compute the remainder of dividing the value in register 0 by the value in register 2, and store the result in register 0
    (7, 0, 0),   # Halt the CPU
]

# Call the function to load your program into the ram
cpu.load_program(program)

# Execute the program by calling the RUN function
cpu.run()

# Show the results that came back from the cpu
print(cpu.registers)
# With the example program the output sould be [0, 0, -1, 0, 5, 0, -7, 0]
