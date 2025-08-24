; ----------------------------------------------------------------------------------------------------
; Title          : ALP to print the stars using times directive (32-bit)
; File Name      : gdbqeza.asm
; Compiled       : NASM version 2.16.03
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

section .data
title db "———————————————————————————"
    db 10, "ALP to print the stars"
    db 10, "———————————————————————————",10
title_len equ $-title

star times 10 db "*"
end db 10, "———————————————————————————",10
end_len equ $-end

section .bss
%macro display 4
    mov eax,%1
    mov ebx,%2
    mov ecx,%3
    mov edx,%4
    int 80h
%endm

section .text
global _start
_start:
    display 4,1,title,title_len
    display 4,1,star,10
    display 4,1,end,end_len

exit:
    mov ebx,0
    mov eax,1
    int 80h
