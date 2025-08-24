; ----------------------------------------------------------------------------------------------------
; Title          : ALP to print the given string using macro (64-bit)
; File Name      : gdwagtz.asm
; Compiled       : NASM version 2.16.03
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

section .data
title db "———————————————————————————————————————————"
    db 10, "ALP to print the given string"
    db 10, "———————————————————————————————————————————",10
title_len equ $-title

input db "Enter the string "
input_len equ $-input

output db 10, "Given string is "
output_len equ $-output

end db "———————————————————————————————————————————",10
end_len equ $-end

section .bss
    string resb 50

%macro display 4
    mov rax,%1
    mov rdi,%2
    mov rsi,%3
    mov rdx,%4
    syscall
%endm

section .text
global _start
_start:
    display 1,1,title,title_len
    display 1,1,input,input_len
    display 0,0,string,50
    display 1,1,output,output_len
    display 1,1,string,50
    display 1,1,end,end_len

exit:
    mov rax,60
    mov rbx,0
    syscall
