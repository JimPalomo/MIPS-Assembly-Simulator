#################################################################
# Project 1: Mips programming with MARS				#
# 1) Generating an array of numbers A1 - A100 			#
# 2) Generating width array W1-W100				#
# 3) Generating the histogram array of the widths H0 - H32	#
# Collaboration by Rafay Usmani, Anas Shalabi, and Jim Palomo	#
#################################################################

# Given -------------------------------------------------------------------------------------------------------------
addi $8, $0, 5        		# A = 5
addi $9, $0, -6    		# B = -6
lui $10, 0xCD     		# C = 0x00CD0000
ori $10, $10, 0x1234   		# C = 0x00CD1234 

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Part 1	Generating an array of numbers A1 - A100							/////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Start here --------------------------------------------------------------------------------------------------------
addi $11, $0, 8352    		# $11 = 8352
addi $12, $0, 8752     		# $12 = 8524; last data segment for part 1 will be 8352 + 400 = 8752
            			# note that 400 came from 100 (size of array) * 4 (bytes per data segment).
addi $15, $0, 1			# $15 = 1
				# $25 = 0

Loop:
mul $8, $8, $9        		# A(n) = A(n) * B [n = each loop iteration]
mfhi $13			# $13 = hi
bne $25, $13, overflow		# if $25 = $13 [1=1] then there is an overflow so branch
xor $8, $8, $10			# $8 = (A * B) xor C
j updateMemory			# branch to updateMemory

overflow:
mflo $8				# lower 32 bit (lo)
xor $8, $8, $10			# $8 = (A * B) xor C
j updateMemory			# branch to updateMemory

updateMemory:
sw $8, 0($11)			# DM[$11] = $8
addi $11, $11, 4    		# update memory location (+4) to form array
bne $11, $12, Loop    		# stop when reached 100 element in Part 1 array 

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Part 2	Generating width array W1-W100									/////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
addi $13, $0, 8328		# $13 = hold address for current 32 bit
addi $14, $0, 31		# $14 = 31 (for first loop, holds far left 1 bit position)
addi $15, $0, 1			# $15 = 1 (checks)

				# $9 = temporary counter
				# $10 = hold current 32 bit  
				# $11 = used to check bit before loops (MSB / LSB)hold scanned bit / temp
				# $12 = hold width 
				# $24 = 0 [counter for first right shifts]
				# $25 = 0 [counter for second right shifts]


addi $1, $0, 8864		# $1 = 8864	DM[W] start 
addi $2, $0, 9264		# $2 = 9264	DM[W] end
addi $8, $0, 8352		# $8 = 8352	DM[A] start
sub $9, $9, $9			# reset $9
addi $7, $0, 8192		# $7 = 8192 	DM[H] start
addi $4, $0, 4			# $4 = 4

# Start Looping here after implementation
Loop_Part2_3:
lw $3, 0($8)			# $3 = DM[$8] = DM[8352] (start of A-array)		
												
addi $10, $3, 0			# reset $10 to original 32 bit

# Check for zero case [Special Case #1] -----------------------------------------------------------------------------
beq $10, $0, sp_case1

# Check for only 1 one [Special Case #2] ----------------------------------------------------------------------------
addi $10, $3, 0			# reset $10 to original 32 bit

lui $24, 0x8			# $24 = 0x00008000
sll $24, $24, 12		# $24 = 0x80000000 = 10000...0

addi $25, $0, 2			# $25 = 2

				# check 0x80000000; signed so we have to check for negative
				
beq $10, $24, sp_case2 		# check if $8 (given) is $24 (0x80000000 = -2147483648)
srl $24, $24, 1

case_two_loop:
beq $10, $24, sp_case2		# check if $8 (given) is $24 (where $24 is a 2^n value)
srl $24, $24, 1
addi $9, $9, 1			# temporary counter
bne $9, $14, case_two_loop	# once $9 gets to 31 (iterations) stop 

# Reset $9 = 0, $15 = 1, $24 = 0, $25 = 0 ---------------------------------------------------------------------------
sub $9, $9, $9			# reset $9 to 0
addi $15, $0, 1			# reset $15 to 1 ($15 = $15 + 2 = -1 + 2 = 1)
sub $24, $24, $24 		# reset $24 to 0
sub $25, $25, $25 		# reset $24 to 0

# Check for 1 @ MSB & LSB for original [Special Case 3] -------------------------------------------------------------
lui $9, 0x8000			# $8 = 0x80000000		
ori $9, $9, 1			# $8 = 0x80000001 = 1000...01
beq $9, $8, sp_case3	

# Reset $9  ---------------------------------------------------------------------------------------------------------
sub $9, $9, $9			# reset $9 = 0

# Far_Left (1st Right Shifting Loop) --------------------------------------------------------------------------------																								
Far_Left:
addi $10, $3, 0			# reset $10 to original 32 bit
srlv $10, $10, $14		# set [31 - # iterations] to LSB
addi $24, $24, 1		# $24 = counter for # of shifts
andi $10, $10, 1		# check shifted [MSB - # iterations] if it is a 1 or 0 by zero extend 
				# (e.g. 01001011 --> 00000001)
addi $14, $14, -1		# $14 = 31 - # iterations (set up for next iteration)
bne $10, $15, Far_Left		# branch until 1 is found

# Check for 1 at LSB before Far_Right  -------------------------------------------------------------------------------																								
addi $10, $3, 0			# reset $10 to original 32 bit
andi $11, $10, 1		# check LSB to see if shifting is needed
beq $11, $15, skip_right

# Far_Right (2nd Right Shifting Loop) -------------------------------------------------------------------------------																								
addi $10, $3, 0			# reset $10 to original 32 bit
Far_Right:
srl $10, $10, 1			# right shift data 
andi $11, $10, 1		# $11 = stores LSB of $10
addi $25, $25, 1		# increment second right shift counter
bne $11, $15, Far_Right		# branch if 1 is not found by right shifting
j past_skip_right_cond

skip_right:
addi $25, $0, 0			# set $25 to 0 since no shifts 

past_skip_right_cond:

# Use Equation Here [Width = 31 - X - Y + 2] ------------------------------------------------------------------------
sub $14, $14, $14		# reset $14 to 0
addi $14, $14, 31		# $14 = 31
sub $14, $14, $24		# 31 - $24
sub $14, $14, $25		# 31 - $24 - $25
addi $12, $14, 2		# 31 - $24 - $25 + 2 --> WIDTH	

j next_set

sp_case1:			# [Special Case: 1]
addi $12, $0, 0			# since the 32 bit totals to 0, then there are no 1 bits so width is 0
j next_set			# jump for next iteration

sp_case2:			# [Special Cases: 2, 4, 5]
addi $12, $0, 1			# set width to 1 since there is only 1 bit in the 32 bit original
j next_set			# jump for next iteration

sp_case3: 			# [Special Case 3]
addi $12, $0, 32		# set width to 32 since there is only two 1's @ MSB and LSB
j next_set			# jump for next iteration

next_set:

# Set up next loop here
addi $14, $0, 31		# reset $14 to 31
sw $12, 0($1)			# store $12
addi $1, $1, 4			# update memory address by +4 for next iteration
addi $8, $8, 4			# update memory address by +4 for next iteration

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Part 3	Generating the histogram array of the widths H0 - H32						/////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

mul $5, $12, $4			# $5 (offset) = $12 * $4 = Width * 4 (data memory represented ending in 4's)
add $7, $7, $5 			# add base + offset
lw $6 0($7)			# load current count of width
addi $6, $6, 1			# increment value from DM[width]
sw $6 0($7)			# store incremented value from DM[width]
addi $7, $0, 8192		# reset $7 [start of H]
bne $1, $2, Loop_Part2_3	# loop until all elements in W array are accounted for

