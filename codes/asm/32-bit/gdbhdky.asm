; ----------------------------------------------------------------------------------------------------
; Title          : ALP to print Hello World using times directive (32-bit)
; File Name      : gdbhdky.asm
; Compiled       : NASM version 2.16.03
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

section .data
h times 60 db "Hello, World!",10

section .text
global _start
_start:
    mov eax,4
    mov ebx,1
    mov ecx,h
    mov edx,60
    int 80h

;Exit System Call
    mov eax,1
    mov ebx,0
    int 80h
