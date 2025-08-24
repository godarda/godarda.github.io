; ----------------------------------------------------------------------------------------------------
; Title          : ALP to print Hello World using macro (64-bit)
; File Name      : gdsgpyl.asm
; Compiled       : NASM version 2.16.03
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

section .data
msg db "Hello, World!",10
msg_len equ $-msg

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
    display 1,1,msg,msg_len

;Exit System Call
    mov rax,60
    mov rbx,00
    syscall
