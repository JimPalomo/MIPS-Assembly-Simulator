# MIPS-Assembly-Simulator

### Description:
MIPS Assembly Simulator in Python. The following project takes in MIPS machine code (hex) and simulates the operation. 

### Program Includes:
- 32 registers including pc, hi, and lo
- Data memory ranging from memory address 0x2000 - 0x3000 (data memory scaling is available but limited range for demonstration purposes)
- Special instruction (find width: gets the width of a 32-bit binary string. [e.g. 1000010 = 6])
- Instruction statistics representing alu, jump, branch, memory, and other instructions
- Displayed outputs: step-by-step detailed executions, registers (32 unique), data memory (0x2000 - 0x3000)
- Displayed data memory contains customization options: Decimal/Hexadecimal Address and Decimal/Hexadecimal Values (4 interchangeable modes)

### Instructions:
1. Write MIPS machine code in MARS MIPS Simulator (http://courses.missouristate.edu/kenvollmar/mars/).
2. Convert MIPS code by assembling in MARS > File > Dump Memory to File > Memory Segment = .text, Dump Format = Hexadecimal Text.
3. Make sure the MIPS hex code is in the same workspace as the simulator.py file
4. Run simulator.py and enter desired hex file and output file.

### Example:
![alt text](https://github.com/JimPalomo/MIPS-Assembly-Simulator/blob/main/assets/sample-1.png)
![alt text](https://github.com/JimPalomo/MIPS-Assembly-Simulator/blob/main/assets/sample-2.png)
![alt text](https://github.com/JimPalomo/MIPS-Assembly-Simulator/blob/main/assets/sample-3.png)
![alt text](https://github.com/JimPalomo/MIPS-Assembly-Simulator/blob/main/assets/sample-4.png)