#################################################################
# Project 1: Mips programming with MARS				#
# 1) Generating an array of numbers A1 - A100 			#
# 2) Generating width array W1-W100				#
# 3) Generating the histogram array of the widths H0 - H32	#
# Collaboration by Rafay Usmani, Anas Shalabi, and Jim Palomo	#
#################################################################

# Given -------------------------------------------------------------------------------------------------------------
addi $8, $0, 8        		# A = 5
addi $9, $0, -5     		# B = -6
lui $10, 0xCD         	# C = 0x00CD0000
ori $10, $10, 0xFF   		# C = 0x00CD1234 

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

# fw $12, $3
addi $0, $0, 0

# Set up next loop here
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

