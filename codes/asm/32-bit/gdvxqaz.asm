; ----------------------------------------------------------------------------------------------------
; Title          : ALP to print Hello World (32-bit)
; File Name      : gdvxqaz.asm
; Compiled       : NASM version 2.16.03
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

section .data
msg db "Hello, World!",10
msg_len equ $-msg

section .text
global _start
_start:
    mov eax,4
    mov ebx,1
    mov ecx,msg
    mov edx,msg_len
    int 80h

;Exit System Call
    mov eax,1
    mov ebx,0
    int 80h
