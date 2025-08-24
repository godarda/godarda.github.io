; ----------------------------------------------------------------------------------------------------
; Title          : ALP to convert the hexadecimal to BCD number (64-bit)
; File Name      : gdvnyvi.asm
; Compiled       : NASM version 2.16.03
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

section .data
title db "———————————————————————————————————————————"
    db 10, "ALP to convert the hexadecimal to BCD number"
    db 10, "———————————————————————————————————————————"
    db 10, "Enter 4 digit hexadecimal numaber "
title_len equ $-title

output db 10, "Binary Coded Decimal equivalent is "
output_len equ $-output

end db 10, "———————————————————————————————————————————",10
end_len equ $-end

section .bss
    hex resb 05
    bcd resb 05

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
    display 0,0,hex,5

    mov bx,0
    mov rcx,04
    mov rsi,hex

up1:
    rol bx,04
    mov al,[rsi]
    cmp al,39h
    jbe skip1
    sub al,07h

skip1:
    sub al,30h
    add bl,al
    inc rsi
    loop up1

    mov rcx,5
    mov ax,bx
    mov bx,10

h2b1:
    mov dx,0
    div bx
    push rdx
    loop h2b1
    mov rdi,bcd
    mov rcx,5

h2b2:
    pop rdx
    add dl,30h
    mov [rdi],dl
    inc rdi
    loop h2b2

    display 1,1,output,output_len
    display 1,1,bcd,5
    display 1,1,end,end_len

exit:
    mov rax,60
    mov rbx,0
    syscall
