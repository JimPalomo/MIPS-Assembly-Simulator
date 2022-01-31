########################################
# ECE 366 Project 2                    #
# Jim Palomo                           #
########################################

import os.path as Path

# twoscomp: 2's Complement [return binary (string)]    (string -> string)
# Input: s = binary (string)
# Return: 2's complement binary (string)
def twoscomp(s):
    for j in reversed(range(len(s))):
        if s[j] == '1':
            break

    t = ""
    for i in range(0, j, 1):        # flip everything
        t += str(1-int(s[i]))

    for i in range(j, len(s), 1):   # until the first 1 from the right
        t += s[i]

    return t                        # return 2's complement binary (string)
    
# twoscomp_dec: 2's Complement [return decimal (int)]     [use for sign extend]
# Input: b = binary (string)
# Return: 2's complement decimal (int)
def twoscomp_dec(b):

    l = len(b)          # length of bit provided

    x = b[:1].zfill(l)  # save the first bit and fill with 0's until original length
    x = x[::-1]         # flip binary

    x = int(x, 2) * -1  # value of binary (unsigned: 10000..0) * -1

    y = int(b[1:], 2)   # value of binary without the first bit

    x += y              # add up differing values

    return x            # return 2's complement decimal (int)

# bin_to_dec: convert binary (string) to decimal (int)  [use for sign extend]
# Input: binary (string)
# Return: Decimal (int)
def bin_to_dec(b):
    if(b[0]=="0"):
        return int(b, base=2)
    else:        
        return twoscomp_dec(b)


# zero_extend: zero extend / unsigned operation (for specific operations)
# Input: binary (string)
# Return: decimal (int)
def zero_extend(b):
    return int(b, base=2)   # given a binary string, get unsigned decimal

# Integer to binary

# itosbin: convert integer (int) to signed binary (string)
# Input: i = integer (int) | n = # of bits of desired binary
# Return: returns signed binary (string)
def itosbin(i, n):
    s = ""
    if i >= 0:
        s = bin(i)[2:].zfill(n)
    else:
        s = bin(0-i)[2:].zfill(n)
        s = twoscomp(s)

    return s

# hex_to_bin: convert hex (string) to binary (string)
# Input: line = hex (string)
# Return: unsigned binary (string)
def hex_to_bin(line):
    h = line.replace("\n", "")
    i = int(h, base=16)
    b = bin(i)
    b = b[2:].zfill(32)
    return b

# neg_int_to_hex:
# Input: x = input integer (int)
# Return: x = 2's complemented hexadecimal (string)
def neg_int_to_hex(x):
    x = bin(x & 0xffffffff)[2:]
    x = hex(int(x,2))[2:].zfill(8)
    x = "0x" + x

    return x

# int_to_hex: convert an decimal (int) to hex (string)
# Input: x = input integer (int)
# Return: hex (string)
def int_to_hex(x):
    if (x < 0):
        x = neg_int_to_hex(x)
    else:
        x = "0x" + str(hex(x))[2:].zfill(8)

    return x

# processR: process R-type instructions from machine code (string) to hex (string)
# Input: b = 32 bit binary instruction 
# Return: MIPS equivalent instruction in hex (string)
def processR(b): 
    b_op = b[0:6]
    b_rs = b[6:11]
    b_rt = b[11:16]
    b_rd = b[16:21]
    b_sa = b[21:26]
    b_fn = b[26:32]

    asm = ""

    if (b_fn == '100000'):      # ADD
        rs = int((b_rs), base=2)
        rt = int((b_rt), base=2)
        rd = int((b_rd), base=2)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)

        asm = "add " + rd + ", " + rs + ", " + rt 

    elif (b_fn == '100010'):    # SUB
        rs = int((b_rs), base=2)
        rt = int((b_rt), base=2)
        rd = int((b_rd), base=2)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)

        asm = "sub " + rd + ", " + rs + ", " + rt 

    elif (b_fn == '101010'):    # SLT
        rs = int((b_rs), base=2)
        rt = int((b_rt), base=2)
        rd = int((b_rd), base=2)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)

        asm = "slt " + rd + ", " + rs + ", " + rt 

    elif (b_fn == '000000'):    # SLL
        rt = int((b_rt), base=2)
        rd = int((b_rd), base=2)
        sa = int((b_sa), base=2)

        rt = "$" + str(rt)
        rd = "$" + str(rd)
        sa = str(sa)

        asm = "sll " + rd + ", " + rt + ", " + sa

    elif (b_fn == '100110'):    # XOR
        rs = int((b_rs), base=2)
        rt = int((b_rt), base=2)
        rd = int((b_rd), base=2)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)

        asm = "xor " + rd + ", " + rs + ", " + rt 

    elif (b_fn == '000010'):    # SRL
        rt = int((b_rt), base=2)
        rd = int((b_rd), base=2)
        sa = int((b_sa), base=2)

        rt = "$" + str(rt)
        rd = "$" + str(rd)
        sa = str(sa)

        asm = "srl " + rd + ", " + rt + ", " + sa

    elif (b_fn == '000110'):    # SRLV
        rs = int((b_rs), base=2)
        rt = int((b_rt), base=2)
        rd = int((b_rd), base=2)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)

        asm = "srlv " + rd + ", " + rt + ", " + rs
    
    elif (b_fn == '100001'):    # ADDU
        rs = int((b_rs), base=2)
        rt = int((b_rt), base=2)
        rd = int((b_rd), base=2)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)

        asm = "srlv " + rd + ", " + rs + ", " + rt

    elif (b_fn == '010000'):    # MFHI
        rd = int((b_rd), base=2)        
        rd = "$" + str(rd)

        asm = "mfhi " + rd

    elif(b_fn == '010010'):     # MFLO  
        rd = int((b_rd), base=2)        
        rd = "$" + str(rd)

        asm = "mflo " + rd

    else:
        print (f'NO idea about op = {b_fn}')
    return asm
    
# processI: process I-type instructions from machine code (string) to hex (string)
# Input: b = 32 bit binary instruction 
# Return: MIPS equivalent instruction in hex (string)
def processI(b):
    b_op = b[0:6]
    b_rs = b[6:11]
    b_rt = b[11:16]
    b_imm = b[16:]

    asm = ""

    if(b_op == '001000'):       # ADDI
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "addi "+ rt + ", " + rs + ", " + imm

    elif (b_op == '001100'):    # ANDI
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = zero_extend(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "andi "+ rt + ", " + rs + ", " + imm

    elif (b_op == '100011'):    # LW
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "lw "+ rt + ", " + imm + "(" + rs + ")"

    elif (b_op == '101011'):    # SW
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "sw "+ rt + ", " + imm + "(" + rs + ")"

    elif (b_op == '000100'):    # BEQ
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "beq "+ rs + ", " + rt + ", " + imm

    elif (b_op == '000101'):    # BNE
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "bne "+ rs + ", " + rt + ", " + imm

    elif (b_op == '001101'):    # ORI
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = zero_extend(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "ori "+ rt + ", " + rs + ", " + imm    

    elif (b_op == '001110'):    # XORI
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = zero_extend(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "xori "+ rt + ", " + rs + ", " + imm                

    elif (b_op == '001111'):    # LUI
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)
        
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "lui "+ rt + ", " + imm
    
    elif (b_op == '111111'):    # FW [Special Instruction]
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)

        rs = "$" + str(rs)
        rt = "$" + str(rt)

        asm = "fw "+ rt + ", " + rs 

    else:
        print (f'NO idea about op = {b_op}')
    return asm

# processJ: process J-type instructions from machine code (string) to hex (string)
# Input: b = 32 bit binary instruction 
# Return: MIPS equivalent instruction in hex (string)
def processJ(b): 
    b_op = b[0:6]
    b_imm = b[6:]

    asm = ""
    
    imm = bin_to_dec(b_imm)
    imm = str(imm)
    asm = "j " + imm
    
    return asm

# processMUL: process MUL instruction from machine code (string) to hex (string) [treated differently than MULT / NOT R, I, J Type]
# Input: b = 32 bit binary instruction 
# Return: MIPS equivalent instruction in hex (string)
def processMUL(b):
    b_rs = b[6:11]
    b_rt = b[11:16]
    b_rd = b[16:21]
    b_sa = b[21:26]
    b_fn = b[26:32]

    asm = ""      
    
    rs = int((b_rs), base=2)
    rt = int((b_rt), base=2)
    rd = int((b_rd), base=2)
    rs = "$" + str(rs)
    rt = "$" + str(rt)
    rd = "$" + str(rd)

    asm = "mul " + rd + ", " + rs + ", " + rt 

    return asm  

# process: determine whether the process provided by machine code (string) is MUL, R, I, or J type.
# Input: b = 32 bit binary instruction 
# Return: MIPS equivalent instruction in hex (string) after determining instruction type
def process(b):
    b_op = b[0:6]
    b_fn = b[26:32]

    if (b_op == '011100' and b_fn == '000010'):  # MUL (special case due to MARS simulator, non-psuedo)
        return processMUL(b)
    elif (b_op == '000000'):        # R-type
        return processR(b)
    elif (b_op == '000010'):        # J-type
        return processJ(b)
    else:                           # I-type
        return processI(b)

# disassemble: disassembles 32 bit instructions from input .txt file and appends spliced instruction to a list
# Input: input_file = input .txt file (of 32-bit machine code) | asm_instr = output .txt file (hex equivalent of machine code) 
# Return: list (instr) of all instructions from .txt file
def disassemble(input_file, asm_instr):
    instr = []    # create empty list of user inputs

    ''' reasons for list: 
            1. able to append at the end of list to KEEP ORDER
            2. mutable (change elements in list if necessary)
            3. creating a list data structure using string methods (replace, split)
    '''

    line_count = 0

    # convert 32 bit machine code from input and write to output file
    for line in input_file:
        line_count += 1
        bin_str = hex_to_bin(line)
        asmline = process(bin_str) 
        output_file.write(asmline + '\n')

        # splice asmline using string methods and append spliced instruction to list
        asm_instr.append(asmline)                   # save asmline into asm_instr
        asmline = asmline.replace("j", "j,")        # remove j and replace w/ "j,"
        asmline = asmline.replace(", $", ",")       # remove middle $ and replace w/ ","
        asmline = asmline.replace(" $", ",")        # remove first $ and replace w/ ","
        asmline = asmline.replace(")", ",")         # remove ")" and replace w/ ","        
        asmline = asmline.replace(" ", "")          # remove extra spacing
        asmline = asmline.replace("($", ",")        # remove "($" and replace w/ ","
        asmline = asmline.split(",")                # split by "," and generate a list
        instr.append(asmline)                       # append to another list which results in a list-list data structure

    output_file.write("\n") # newline in output file to show finished
    input_file.close()      # close input file since we no longer need it

    return instr          # return list of listed spliced instructions (list-list) to main

# itosbin: convert decimal/integer (int) to binary (string)
# Input: i = decimal/integer (int) | n = amount of bits input (int)
# Return: (signed) binary string
def itosbin(i, n):
    s = ""
    if i >= 0:
        s = bin(i)[2:].zfill(n)
    else:
        s = bin(0-i)[2:].zfill(n)
        s = twoscomp(s)

    return s

# and32: perform logic AND on two 32 bit binary (strings)
# Input: x, y = 32-bit binary (strings)
# Return: ANDed binary string
def and32(x, y):
    s = ""
    for i in range(32):
        if (x[i] == '1') and (y[i] == '1'):
            s += '1'
        else:
            s += '0'
    
    return s

# or32: perform logic OR on two 32 bit binary (strings)
# Input: x, y = 32-bit binary (strings)
# Return: ORed binary string
def or32(x, y):
    s = ""
    for i in range(32):
        if (x[i] == '1') or (y[i] == '1'):
            s += '1'
        else:
            s += '0'
    
    return s

# xor32: perform logic XOR on two 32 bit binary (strings)
# Input: x, y = 32-bit binary (strings)
# Return: XORed binary string
def xor32(x, y):
    s = ""
    for i in range(32):
        if x[i] == y[i]:
            s += '0'
        else:
            s += '1'
    
    return s

# lui32: load upper immediate
# x = integer (string) | return = lui of x (int)

# lui32: load upper immediate of 
# Input: x = decimal (string)
# Return: decimal (int)
def lui32(x):
    x = int(x) << 16
    x = itosbin(x, 32)
    x = bin_to_dec(x)
    return x

# j_pc_count: perform PC calculation for j jump instruction
# Input: pc = current value of PC before jump | addr = address from j-type 32 bit instruction
# Return: new value of PC (int)
def j_pc_count(pc, addr):
    # Eqn: pc = (pc & 0xf0000000) | (addr << 2)

    a = itosbin(pc, 32)
    b = '11110000000000000000000000000000'  # 0xf0000000
    c = and32(a,b)
    
    d = itosbin(addr << 2, 32)
    
    z = or32(c, d)

    z = bin_to_dec(z)

    return z

# accessDM: hash function for accessing data memory [O(1) access]
# Input: s = hex or integer/decimal (string)
# Return: data memory location of the data memory array
def accessDM(s):
    if (s[2:] == "0x"):
        s = int(s, base=16)
    else:
        s = int(s)

    s = int((s - 0x2000) / 4)
    
    return s

# outputRegisters: output all 32 registers + pc, hi, lo 
# Input: reg = array holding register data | pc, hi, lo = special registers
# Return: outputted registers via console & output file
def outputRegisters(reg, pc, hi, lo, hexValue):
    pReg = "Register"
    pVal = "Value"
    print(f"{pReg:<15}{pVal:^12}")

    # output header output file
    row_item = [pReg, pVal]
    output = '{:<15}{:^12}'.format(row_item[0], row_item[1])
    output_file.write(output + "\n")

    # output 32 registers from reg array 
    for i in range(len(reg)):
        pReg = "$" + str(i)
        if (hexValue == 0):
            pVal = str(reg[i])
        else:
            pVal = int_to_hex(reg[i])
        print(f"{pReg:<15}{pVal:>12}")
        
        # output to txt file
        row_item = [pReg, pVal]
        output = '{:<15}{:>12}'.format(row_item[0], row_item[1])
        output_file.write(output + "\n")        

    # output special registers
    pReg = "pc"
    if (hexValue == 0):
        pVal = str(pc)
    else:
        pVal = int_to_hex(pc)  

    print(f"{pReg:<15}{pVal:>12}")

    row_item = [pReg, pVal] # output to txt file
    output = '{:<15}{:>12}'.format(row_item[0], row_item[1])
    output_file.write(output + "\n")     

    pReg = "hi"
    if (hexValue == 0):
        pVal = str(hi)
    else:
        pVal = int_to_hex(hi)    
    print(f"{pReg:<15}{pVal:>12}")

    row_item = [pReg, pVal] # output to txt file
    output = '{:<15}{:>12}'.format(row_item[0], row_item[1])
    output_file.write(output + "\n") 

    pReg = "lo"
    if (hexValue == 0):
        pVal = str(lo)
    else:
        pVal = int_to_hex(lo) 
    print(f"{pReg:<15}{pVal:>12}")

    row_item = [pReg, pVal] # output to txt file
    output = '{:<15}{:>12}'.format(row_item[0], row_item[1])
    output_file.write(output + "\n" + "\n") 

    print("\n")


# outputDataMem: output data memory array in similar format as MARS
# Input: mem = data memory array | hex_start = starting memory address | hex_end = ending memory address 
#        address = user selected hex or decimal address output |  value = user selected hex or decimal value output
# Output: outputted data memory array in console and output file
def outputDataMem(mem, hex_start, hex_end, address, value):
    addr = v1 = v2 = v3 = v4 = v5 = v6 = v7 = v8 = ""

    # headers
    if (address == 0):      # [decimal address]
        addr = "Address"
        v1 = "Value (+0)"
        v2 = "Value (+4)"
        v3 = "Value (+8)"
        v4 = "Value (+12)"
        v5 = "Value (+16)"
        v6 = "Value (+20)"
        v7 = "Value (+24)"
        v8 = "Value (+28)"

        # output header to output .txt file [decimal]
        row_item = [addr, v1, v2, v3, v4, v5, v6, v7, v8]
        output = '|{:>10}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|'.format(row_item[0], row_item[1], row_item[2], row_item[3], row_item[4], row_item[5], row_item[6], row_item[7], row_item[8])
        output_file.write(output + "\n")

    else:                   # [hexadecimal address]
        addr = "Address"
        v1 = "Value (+0)"
        v2 = "Value (+4)"
        v3 = "Value (+8)"
        v4 = "Value (+c)"
        v5 = "Value (+10)"
        v6 = "Value (+14)"
        v7 = "Value (+18)"
        v8 = "Value (+1c)"

        # output header to output .txt file [hex]
        row_item = [addr, v1, v2, v3, v4, v5, v6, v7, v8]
        output = '|{:^10}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|'.format(row_item[0], row_item[1], row_item[2], row_item[3], row_item[4], row_item[5], row_item[6], row_item[7], row_item[8])
        output_file.write(output + "\n")

    print(f"|{addr:>15}|{v1:>15}|{v2:>15}|{v3:>15}|{v4:>15}|{v5:>15}|{v6:>15}|{v7:>15}|{v8:>15}|")

    j = 0

    if (value == 0):        # data memory [decimal values]
        for i in range(hex_start, hex_end, 4):
            if (j % 8 == 0):
                if (address == 1):
                    addr = "0x" + str(hex(j*4 + 0x2000))[2:].zfill(8)
                else:
                    addr = str(j*4 + 0x2000)

                if j < len(mem):
                    v1 = str(mem[j]) 
                else:
                    v1 = 0
    
                if j+1 < len(mem):
                    v2 = str(mem[j+1]) 
                else:
                    v2 = 0
    
                if j+2 < len(mem):
                    v3 = str(mem[j+2]) 
                else:
                    v3 = 0
    
                if j+3 < len(mem):
                    v4 = str(mem[j+3]) 
                else:
                    v4 = 0
    
                if j+4 < len(mem):
                    v5 = str(mem[j+4]) 
                else:
                    v5 = 0
    
                if j+5 < len(mem):
                    v6 = str(mem[j+5]) 
                else:
                    v6 = 0
    
                if j+6 < len(mem):
                    v7 = str(mem[j+6]) 
                else:
                    v7 = 0
    
                if j+7 < len(mem):
                    v8 = str(mem[j+7]) 
                else:
                    v8 = 0
    
                print(f"|{addr:>15}|{v1:>15}|{v2:>15}|{v3:>15}|{v4:>15}|{v5:>15}|{v6:>15}|{v7:>15}|{v8:>15}|")
                row_item = [addr, v1, v2, v3, v4, v5, v6, v7, v8]
                output = '|{:>10}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|'.format(row_item[0], row_item[1], row_item[2], row_item[3], row_item[4], row_item[5], row_item[6], row_item[7], row_item[8])
                output_file.write(output + "\n")    

            j += 1

    else:        # data memory [hexadecimal values]
        for i in range(hex_start, hex_end, 4):
            if (j % 8 == 0):
                if (address == 1):
                    addr = "0x" + str(hex(j*4 + 0x2000))[2:].zfill(8)
                else:
                    addr = str(j*4 + 0x2000)

                if j < len(mem):
                    if (mem[j] < 0):
                        v1 = neg_int_to_hex(mem[j])
                    else:
                        v1 = "0x" + str(hex(mem[j]))[2:].zfill(8)
                else:
                    v1 = "0x" + "".zfill(8)
    
                if j+1 < len(mem):
                    if (mem[j+1] < 0):
                        v2 = neg_int_to_hex(mem[j+1])
                    else:
                        v2 = "0x" + str(hex(mem[j+1]))[2:].zfill(8)
                else:
                    v2 = "0x" + "".zfill(8)
    
                if j+2 < len(mem):
                    if (mem[j+2] < 0):
                        v3 = neg_int_to_hex(mem[j+2])
                    else:
                        v3 = "0x" + str(hex(mem[j+2]))[2:].zfill(8)
                else:
                    v3 = "0x" + "".zfill(8)
    
                if j+3 < len(mem):
                    if (mem[j+3] < 0):
                        v4 = neg_int_to_hex(mem[j+3])
                    else:
                        v4 = "0x" + str(hex(mem[j+3]))[2:].zfill(8)                
                else:
                    v4 = "0x" + "".zfill(8)
    
                if j+4 < len(mem):
                    if (mem[j+4] < 0):
                        v5 = neg_int_to_hex(mem[j+4])
                    else:
                        v5 = "0x" + str(hex(mem[j+4]))[2:].zfill(8)
                else:
                    v5 = "0x" + "".zfill(8)
    
                if j+5 < len(mem):
                    if (mem[j+5] < 0):
                        v6 = neg_int_to_hex(mem[j+5])
                    else:
                        v6 = "0x" + str(hex(mem[j+5]))[2:].zfill(8)
                else:
                    v6 = "0x" + "".zfill(8)
    
                if j+6 < len(mem):
                    if (mem[j+6] < 0):
                        v7 = neg_int_to_hex(mem[j+6])
                    else:
                        v7 = "0x" + str(hex(mem[j+6]))[2:].zfill(8)
                else:
                    v7 = "0x" + "".zfill(8)
                    
    
                if j+7 < len(mem):
                    if (mem[j+7] < 0):
                        v8 = neg_int_to_hex(mem[j+7])
                    else:
                        v8 = "0x" + str(hex(mem[j+7]))[2:].zfill(8)
                else:
                    v8 = "0x" + "".zfill(8)
    
                print(f"|{addr:>15}|{v1:>15}|{v2:>15}|{v3:>15}|{v4:>15}|{v5:>15}|{v6:>15}|{v7:>15}|{v8:>15}|")
                row_item = [addr, v1, v2, v3, v4, v5, v6, v7, v8]
                output = '|{:<10}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|'.format(row_item[0], row_item[1], row_item[2], row_item[3], row_item[4], row_item[5], row_item[6], row_item[7], row_item[8])
                output_file.write(output + "\n")      



            j += 1            
    print("\n")

# outputInstrStats: output instruction statistics (ALU, Jump, branch, memory, other)
# Input: total, alu, jump, branch, memory, other = current values that are held for each count variable
# Return: output instruction statistics on console and output .txt file 
def outputInstrStats(total, alu, jump, branch, memory, other):
    print("Instruction Statistics, Version 1.0")
    output_file.write("\n\nInstruction Statistics, Version 1.0" + "\n")

    print(f"Total:\t{total}\n")
    output_file.write(f"Total:\t{total}\n\n")

    titles = ["ALU:", "Jump:", "Branch:", "Memory:", "Other:"]
    values = [alu, jump, branch, memory, other]
    percentages = [(alu/total)*100, (jump/total)*100, (branch/total)*100, (memory/total)*100, (other/total)*100]
    i = 0
    while i < len(titles):
        print(f"{titles[i]:<8}{values[i]:<8}{percentages[i]:.0f}%")
        output_file.write(f"{titles[i]:<8}{values[i]:<8}{percentages[i]:.0f}%" + "\n")

        i += 1
   
# findWidth: special instruction used to find the width of a 32-bit binary code
# Input: s = decimal (string)
# Return: width of the specific decimal translated in 32-bit binary 
def findWidth(s):               # take in decimal string 
    b = int(s)                  # convert string decimal to int decimal
    b = itosbin(b, 32)          # convert integer to binary
    return len(b.strip("0"))    # strip surrounding zeros from 1...1 & return length of remaining bits

# mul: multiplication instruction (non R, J, I type) but special non-psuedo instruction
# Input: x, y = decimal values (int)
# Output: decimal pair (int, int) (hi 32bit, lo 32bit)
def mul(x, y):
    product = x * y
    z = itosbin(product, 64)
    mhi, mlo = z[:len(z)//2], z[len(z)//2:]

    return bin_to_dec(mhi), bin_to_dec(mlo)

# srl: bit shift right by n amounts
# Input: b = binary (string) | n = amount of shifts (integer) 
# Output: bit shifted decimal (integer)
def srl(b, n):
    r = 32 - n
    b = b[0:r].zfill(32)

    return bin_to_dec(b)

# sll: bit shift left by n amounts
# Input: b = binary (string) | n = amount of shifts (integer) 
# Output: bit shifted decimal (integer)
def sll(b, n):
    b = b[n:32].ljust(32, '0')

    return bin_to_dec(b)


# Main ------------------------------------------------------------------------------------------

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Project 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

input_file = input("Enter input file> ")                # ask for user input file

file_exists = 0                                         # temp variable to keep track of file exist state 

# check if input file exists 
while (file_exists != 1):
    if Path.isfile(input_file): # file exists
        print("File sucessfully loaded")
        input_file = open(input_file, "r")              # open input file in read mode (r)
        file_exists = 1                                 # file exists so set true
    else: # file does not exist, so ask for valid file
        print("File does not exist")
        file_exists = 0                                 # file does not exists so set false
        input_file = input("Enter input file> ")

output_file = input("Enter desired output file> ")      # ask for user output file name
output_file = open(output_file,"w")                     # create and open output file in write mode (w)

choice1 = choice2 = hexAddress = hexValue = 0

print("\nWhat data representation would you like?")
while (choice1 == 0 and choice2 == 0):
    x = input("Hexadecimal Address? (y = yes, n = no)> ")
    while (choice1 == 0) and (x != 'y' or x != 'n'):
        if (x == 'y'):
            hexAddress = 1
            choice1 = 1
        elif (x == 'n'):
            choice1 = 1
            break
        else:
            x = input("Hexadecimal Address? (y = yes, n = no)> ")
            continue

    y = input("Hexadecimal Values? (y = yes, n = no)> ")
    while (choice2 == 0) and (x != 'y' or x != 'n'):
        if (y == 'y'):
            hexValue = 1
            choice2 = 1
        elif (y == 'n'):
            choice2 = 1
            break
        else:
            y = input("Hexadecimal Value? (y = yes, n = no)> ")
            continue

print("\n")
# hardcoded for testing purposes
# input_file = open("test_files/project1_edit.txt", "r")
# output_file = open("test_files/asm.txt", "w")

asm_instr = []                                          # save default asm instruction

instr = disassemble(input_file, asm_instr)              # disassemble machine code from input file to readable MIPS
                                                        # place results into a list data structure; holds line number [starting at 0 for 1]

# registers
reg = [0] * 32              # create register from $0 to $31 (w/ pc, lo, hi)
pc = hi = lo = line = 0     # line = current instruction line number

# data memory
mem = [0] * 1024             # (0x3000 - 0x2000) / 4 = 1024 memory cells

# instruction statistics
total = alu = jump = branch = memory = other = 0

# output header
pLine = "line"
pInstr = "Instruction"
pResult = "Result"
pPC = "PC"

print(f"{pLine:<15}{pInstr:<35}{pResult:<25}{pPC:<15}")

# output header to output .txt file
row_item = [pLine, pInstr, pResult, pPC]
output = '{:<8}{:<24}{:<26}{:<8}'.format(row_item[0], row_item[1], row_item[2], row_item[3])

output_file.write(output + "\n")

# analyze instructions
while (int(pc/4) < len(instr)):     # int(pc/4) = current instruction
    cur = instr[int(pc/4)]          # give access to instr[] list-list
                                    # first list: separated machine code instructions (access to opcode, rs, rt, rd, sa, func, imm)
                                    # second list: holds the first list within itself and replicates "line numbers"

    line += 1                       # update for next instruction in instr list

    # instructions 
    
    # branch instructions 
    if (cur[0] == "j" or cur[0] == "beq" or cur[0] == "bne"):

        if (cur[0] == 'j'):         # J
            pInstr = asm_instr[int(pc/4)]
            pc = j_pc_count(pc, int(cur[1]))
            jump += 1

        elif (cur[0] == "beq"):     # BEQ
            if (reg[int(cur[1])] == reg[int(cur[2])]):
                pInstr = asm_instr[int(pc/4)]                
                pc += 4 + (int(cur[3]) << 2)
            else:
                pInstr = asm_instr[int(pc/4)]
                pc += 4

            branch += 1

        else:                       # BNE
            if (reg[int(cur[1])] != reg[int(cur[2])]):
                pInstr = asm_instr[int(pc/4)]
                pc += 4 + (int(cur[3]) << 2)
            else:
                pInstr = asm_instr[int(pc/4)]
                pc += 4  

            branch += 1

        # update result
        if (cur[0] == "beq" or cur[0] == "bne"):
            pResult = "branch to PC: " + str(pc) 
        else:
            pResult = "jump to PC " + str(pc)
     
    # must be sw/lw
    elif (cur[0] == "sw" or cur[0] == "lw"):
        if (cur[0] == "sw"):    # SW
            mem[accessDM(str(int(cur[2]) + reg[int(cur[3])]))] = reg[int(cur[1])]
            pResult = "DM[" + str(int(cur[2]) + reg[int(cur[3])]) + "]" + " = " + str(reg[int(cur[1])])

        else:                   # LW
            reg[int(cur[1])] = mem[accessDM(str(int(cur[2]) + reg[int(cur[3])]))]
            # update results    

            pResult = "$" + cur[1] + " = " + str(reg[int(cur[1])])

        pc += 4
        pInstr = asm_instr[int(pc/4) - 1]

        memory += 1

    else:   # must not lw/sw or branch instruction
        if (cur[0] == "addi"):      # ADDI
            reg[int(cur[1])] = reg[int(cur[2])] + int(cur[3])      

        elif (cur[0] == "add"):     # ADD
            reg[int(cur[1])] = reg[int(cur[2])] + reg[int(cur[3])]

        elif (cur[0] == "sub"):     # SUB
            reg[int(cur[1])] = reg[int(cur[2])] - reg[int(cur[3])]

        elif (cur[0] == "slt"):     # SLT
            if (reg[int(cur[2])] < reg[int(cur[3])]):  # if x < y 
                reg[int(cur[1])] = 1    # x = 1
            else: # x > y
                reg[int(cur[1])] = 0    # x = 0

        elif (cur[0] == "sll"):     # SLL
            reg[int(cur[1])] = sll(itosbin(reg[int(cur[2])], 32), int(cur[3]))

        elif (cur[0] == "xor"):     # XOR
            reg[int(cur[1])] = reg[int(cur[2])] ^ reg[int(cur[3])]

        elif (cur[0] == "srl"):     # SRL
            reg[int(cur[1])] = srl(itosbin(reg[int(cur[2])], 32), int(cur[3]))

        elif (cur[0] == "srlv"):    # SRLV
            reg[int(cur[1])] = srl(itosbin(reg[int(cur[2])], 32), reg[int(cur[3])])

        elif (cur[0] == "andi"):    # ANDI
            reg[int(cur[1])] = bin_to_dec(and32(itosbin(reg[int(cur[2])], 32), itosbin(int(cur[3]), 32)))
            
        elif (cur[0] == "ori"):     # ORI
            reg[int(cur[1])] = bin_to_dec(or32(itosbin(reg[int(cur[2])], 32), itosbin(int(cur[3]), 32)))

        elif (cur[0] == "xori"):    # XORI
            reg[int(cur[1])] = bin_to_dec(xor32(itosbin(reg[int(cur[2])], 32), itosbin(int(cur[3]), 32)))

        elif (cur[0] == "lui"):     # LUI
            reg[int(cur[1])] = lui32(cur[2])

        elif (cur[0] == "mfhi"):    # MFHI
            reg[int(cur[1])] = hi 

        elif (cur[0] == "mflo"):    # MFLO
            reg[int(cur[1])] = lo
        
        elif (cur[0] == "mul"):     # MUL
            if pInstr.find("$" + cur[3]):
                hi_lo = mul(reg[int(cur[2])], reg[int(cur[3])])    # mul $x, $y
            else:
                hi_lo = mul(reg[int(cur[2])], int(cur[3]))         # mul $x, y

            hi = hi_lo[0]
            lo = hi_lo[1]
            reg[int(cur[1])] = lo

        elif (cur[0] == "fw"):      # FW [Special Instruction]
            reg[int(cur[1])] = findWidth(reg[int(cur[2])])
        
        else:
            print("Instruction not implemented")


        # set $0 as absolute zero
        if (cur[1] == '0'):
            reg[int(cur[1])] = 0    

        # update outputs
        pc += 4

        if (cur[0] == 'slt' or cur[0] == 'mul'):
            other += 1
        else:
            alu += 1

        pResult = "$" + cur[1] + " = " + str(reg[int(cur[1])]) 
        pInstr = asm_instr[int(pc/4) - 1]

    # update print outputs
    pLine = line
    pPC = pc
    
    # print outputs

    print(f"{pLine:<15}{pInstr:<35}{pResult:<25}{pPC:<15}")

    # output to output .txt file
    row_item = [pLine, pInstr, pResult, pPC]
    output = '{:<8}{:<24}{:<26}{:<8}'.format(row_item[0], row_item[1], row_item[2], row_item[3])

    output_file.write(output + "\n")


print("\n")
output_file.write("\n")

# output registers
outputRegisters(reg, pc, hi, lo, hexValue)

# output Data Memory
outputDataMem(mem, 0x2000, 0x3004, hexAddress, hexValue)

# output instruction statistics
total = alu + jump + branch + memory + other
outputInstrStats(total, alu, jump, branch, memory, other)

output_file.close()

print("\nProgram Sucessfully Finished")     # print when program finishes