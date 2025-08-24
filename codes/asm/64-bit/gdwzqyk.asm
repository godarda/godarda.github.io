; ----------------------------------------------------------------------------------------------------
; Title          : ALP to check whether a given string is palindrome (64-bit)
; File Name      : gdwzqyk.asm
; Compiled       : NASM version 2.16.03
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

section .data
title db "———————————————————————————————————————————"
    db 10, "ALP to check string is palindrome or not"
    db 10, "———————————————————————————————————————————",10
title_len equ $-title

input db "Enter the string "
input_len equ $-input

output1 db 10, "Entered string is palindrome"
output1_len equ $-output1

output2 db 10, "Entered string is not palindrome"
output2_len equ $-output2

end db 10, "———————————————————————————————————————————",10
end_len equ $-end

section .bss
    string resb 50
    count resb 01
    reverse resb 01

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

    dec al
    mov [count],al

    mov rcx,0
    mov rsi,string
    mov rdi,reverse
    mov cl,[count]
    add rsi,rcx
    sub rsi,1

up2:
    mov al,[rsi]
    mov [rdi],al
    inc rdi
    dec rsi
    loop up2

    mov rcx,0
    mov rsi,string
    mov rdi,reverse
    mov cl,[count]

up3:
    mov al,[rsi]
    mov bl,[rdi]
    cmp al,bl
    jne exit
    inc rsi
    inc rdi
    loop up3
    display 1,1,output1,output1_len
    display 1,1,end,end_len

    mov rax,60
    mov rbx,0
    syscall

exit:
    display 1,1,output2,output2_len
    display 1,1,end,end_len
 
    mov rax,60
    mov rbx,0
    syscall
