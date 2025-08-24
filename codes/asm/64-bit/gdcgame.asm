; ----------------------------------------------------------------------------------------------------
; Title          : ALP to print the length of a given string (64-bit)
; File Name      : gdcgame.asm
; Compiled       : NASM version 2.16.03
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

section .data
title db "———————————————————————————————————————————"
    db 10, "ALP to print the length of given string"
    db 10, "———————————————————————————————————————————",10
title_len equ $-title

input db "Enter the string "
input_len equ $-input

output db 10, "Length of string "
output_len equ $-output

end db 10, "———————————————————————————————————————————",10
end_len equ $-end

section .bss
    count resd 1
    dispnum resb 8

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
    display 0,0,input,input_len
    mov [count],rax
    display 1,1,output,output_len
    mov rsi,dispnum+7
    mov rax,[count]
    mov rcx,8
    dec rax

cnt:
    mov rdx,0
    mov rbx,10
    div rbx
    add dl,30h
    mov [rsi],dl
    dec rsi
    loop cnt

    display 1,1,dispnum,8
    display 1,1,end,end_len

exit:
    mov rax,60
    mov rbx,0
    syscall
