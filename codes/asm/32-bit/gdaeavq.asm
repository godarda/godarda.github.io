; ----------------------------------------------------------------------------------------------------
; Title          : ALP to print the stars using macro (32-bit)
; File Name      : gdaeavq.asm
; Compiled       : NASM version 2.16.03
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

section .data
title db "———————————————————————————"
    db 10, "ALP to print the stars"
    db 10, "———————————————————————————",10
len: equ $-title

star times 10 db "*"
end db 10, "———————————————————————————",10
end_len equ $-end

section .text
global _start
_start:
    mov eax,4
    mov ebx,1
    mov ecx,title
    mov edx,len
    int 80h

    mov eax,4
    mov ebx,1
    mov ecx,star
    mov edx,10
    int 80h

    mov eax,4
    mov ebx,1
    mov ecx,end
    mov edx,end_len
    int 80h

exit:
    mov ebx,0
    mov eax,1
    int 80h
