<h1>A Simple One Instruction CPU</h1>

<h3>Registers</h3>
<p>The One Instruction CPU has 8 registers, numbered from 0 to 7. Each register is a 32-bit signed integer, capable of holding values between -2147483648 and 2147483647.</p>

<h3>Instructions</h3>
<p>The NANDCPU supports 8 instructions, each identified by an opcode between 0 and 7. Each instruction takes two operands. <br>
{opcode, oprand1, oprand2}  <br>
{opcode, dest reg, oprand2}  <br>
With ADD you can also load data into the registers, example {2, 0, 42} that will put 42 into R2, 0 + 42 = 42 and results will be stored in R0.</p>

<h3>0: MOV</h3>
<p>MOV dest, src copies the value in register src to register dest.</p>

<h3>1: NAND</h3>
<p>NAND (dest, src1, src2) computes the NAND of the values in registers src1 and src2, and stores the result in register dest. 
The NAND of two bits x and y is defined as NOT(x AND y).</p>

<h3>2: ADD</h3>
<p>ADD (dest, src1, src2) adds the value in register src1 to the value in oprand src2, and stores the result in register dest. 
If the result is too large to fit in a 32-bit signed integer, it overflows and wraps around to the smallest representable value.</p>

<h3>3: SUB</h3>
<p>SUB dest, src1, src2 subtracts the value in oprand src2 from the value in register src1, and stores the result in register dest. 
If the result is too small to fit in a 32-bit signed integer, it underflows and wraps around to the largest representable value.</p>

<h3>4: MUL</h3>
<p>MUL dest, src1, src2 multiplies the value in register src1 by the value in oprand src2, and stores the result in register dest. 
If the result is too large to fit in a 32-bit signed integer, it overflows and wraps around to the smallest representable value.</p>

<h3>5: DIV</h3>
<p>DIV dest, src1, src2 divides the value in register src1 by the value in oprand src2, rounding down to the nearest integer, and stores the result in register dest. 
If src2 is zero, the behavior is undefined.</p>

<h3>6: MOD</h3>
<p>MOD dest, src1, src2 computes the remainder of dividing the value in register src1 by the value in oprand src2, and stores the result in register dest. 
If src2 is zero, the behavior is undefined.</p>

<h3>7: HLT</h3>
<p>HLT halts the CPU, causing it to stop executing instructions and return control to the program that called it.</p>

<h3>Execution</h3>
<p>To execute a program, you first need to create a ONE_INSTRUCTION_CPU object using cpu = ONE_INSTRUCTION_CPU(). 
You can then load a program into memory using the load_program method, which takes a list of instructions as its argument. 
You can then execute the program using the run method. When the program completes, the final values of the registers can be retrieved using the registers attribute. 
Note that the NANDCPU does not perform any input/output operations; all data must be supplied to and retrieved from registers. </p>
