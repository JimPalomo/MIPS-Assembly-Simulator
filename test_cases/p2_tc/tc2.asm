addi $8, $0, 1
addi $10, $0, 1
bne $8, $10, L2
L1:
addi $9, $0, -1
lui $1, 1
ori $1, $1, 65535
xor $8, $9, $1
addi $10, $10, -1
beq $10, $0, L2
j L1

L2:
slt $14, $8, $10
