; ----------------------------------------------------------------------------------------------------
; Title          : ALP to print the ASCII hex to hexadecimal number (32-bit)
; File Name      : gdzkizy.asm
; Compiled       : NASM version 2.16.03
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

section .data
title db "———————————————————————————————————————————"
    db 10, "ALP for the ASCII hex to hexadecimal number"
    db 10, "———————————————————————————————————————————",10
len: equ $-title

NO: db 10,30h,31h,32h,33h,34h,35h,36h,37h,38h,39h,41h,42h,43h,44h,45h,46h,47h,10
end db 10, "———————————————————————————————————————————",10
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
    mov ecx,NO
    mov edx,17
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
