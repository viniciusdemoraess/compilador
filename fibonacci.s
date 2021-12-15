.global main
main:
push {ip, lr}       @empilhamento endereco de retorno
MOV R0, #0      @load addres for variable
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =i      @load address
STR R1, [R0]      @store  result
MOV R0, #0      @load addres for variable
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =n      @load address
STR R1, [R0]      @store  result
MOV R0, #0      @load addres for variable
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =auxiliar      @load address
STR R1, [R0]      @store  result
MOV R0, #0      @load addres for variable
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =a      @load address
STR R1, [R0]      @store  result
MOV R0, #1      @load addres for variable
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =b      @load address
STR R1, [R0]      @store  result
LDR R0, =format2       @load addres of pattern number
LDR R1, =n       @load addres of variable
BL scanf  @call function for read
LDR R0, =b      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack result content
pop {R1}         @pops in R1
LDR R0, =format           @load addres of pattern number
BL printf      @call function for print
LDR R0, =n      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
MOV R0, #1      @load number
push {R0}         @stack variable content
pop {R1}          @pops in R1
pop {R0}          @pops in R0
SUB R0, R0, R1    @subtraction operation
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =n      @load address
STR R1, [R0]      @store  result
L3:      @label for `do`
L1:      @label content `do`
LDR R0, =a      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
LDR R0, =b      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R1}          @pops in R1
pop {R0}          @pops in R0
ADD R0, R0, R1    @sum operation
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =auxiliar      @load address
STR R1, [R0]      @store  result
LDR R0, =b      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =a      @load address
STR R1, [R0]      @store  result
LDR R0, =auxiliar      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R1}          @pops in R1
LDR R0, =b      @load address
STR R1, [R0]      @store  result
LDR R0, =auxiliar      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R1}         @pops in R1
LDR R0, =format           @load addres of pattern number
BL printf      @call function for print
LDR R0, =i      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
MOV R0, #1      @load number
push {R0}         @stack variable content
pop {R1}          @pops in R1
pop {R0}          @pops in R0
ADD R0, R0, R1    @sum operation
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =i      @load address
STR R1, [R0]      @store  result
LDR R0, =n      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R0}          @pops R0
MOV R1, R0        @mov content for R1
LDR R0, =i      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R0}      @pops R0
MOV R2, R0        @mov content for r2
CMP R1, R2        @compar contents
BGT L3      @case Val1>Val2
L2:      @label for endDo-while
pop {ip, pc}
.data
.balign 8
format: .asciz "%d\n" 
format2: .asciz "%d" 
.balign 8
i: .word 0
.balign 8
n: .word 0
.balign 8
auxiliar: .word 0
.balign 8
a: .word 0
.balign 8
b: .word 0
.extern printf
.extern scanf
