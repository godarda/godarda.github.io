; ----------------------------------------------------------------------------------------------------
; Title          : ALP to print Hello World without using macro (64-bit)
; File Name      : gdatnak.asm
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
    mov rax,1
    mov rdi,1
    mov rsi,msg
    mov rdx,msg_len
    syscall

;Exit System Call
    mov rax,60
    mov rbx,00
    syscall
