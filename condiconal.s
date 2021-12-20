.global main
main:
push {ip, lr}       @empilhamento endereco de retorno
MOV R0, #2      @load addres for variable
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =maca      @load address
STR R1, [R0]      @store  result
LDR R0, =format2       @load addres of pattern number
LDR R1, =banana       @load addres of variable
BL scanf  @call function for read
MOV R0, #5      @load number
push {R0}         @stack variable content
MOV R0, #8      @load number
push {R0}         @stack variable content
pop {R1}          @pops in R1
pop {R0}          @pops in R0
MUL R0, R0, R1    @multiplication operation
push {R0}         @stack result content
LDR R0, =maca      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R2}          @pops in R1
pop {R1}          @pops in R2
MOV R0, #0        @init variable for resultable
_division:        @create label
SUBS R1, R1, R2   @subtraction operation
ADD R0, R0,#1     @result division
BHI _division     @jump case R1>R2
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =banana      @load address
STR R1, [R0]      @store  result
LDR R0, =banana      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R0}          @pops R0
MOV R1, R0        @mov content for R1
LDR R0, =maca      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R0}      @pops R0
MOV R2, R0        @mov content for r2
CMP R1, R2        @compar contents
BGE L2      @case Val1<Val2
L1:      @label content if
LDR R0, =banana      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R1}         @pops in R1
LDR R0, =format           @load addres of pattern number
BL printf      @call function for print
B L3      @jump for endif
L2:      @label for else
LDR R0, =maca      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R1}         @pops in R1
LDR R0, =format           @load addres of pattern number
BL printf      @call function for print
L3:      @label for endif
pop {ip, pc}
.data
.balign 8
format: .asciz "%d\n" 
format2: .asciz "%d" 
.balign 8
maca: .word 0
.balign 8
banana: .word 0
.extern printf
.extern scanf
