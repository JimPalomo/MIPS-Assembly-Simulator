addi $1, $0, 8192
addi $2, $0, 8236
addi $3, $0, 8380

sw $1, 0($2)
sw $2, 0($3)
sw $3, 0($1)

lw $4, 0($1)
lw $5, 0($2)
lw $6, 0($3)

