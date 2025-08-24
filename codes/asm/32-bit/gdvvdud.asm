; ----------------------------------------------------------------------------------------------------
; Title          : ALP to print the length of a given string (32-bit)
; File Name      : gdvvdud.asm
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
    display 4,1,input,input_len
    display 3,2,input,input_len

    mov [count],eax
    display 4,1,output,output_len

    mov esi,dispnum+7
    mov eax,[count]
    mov ecx,8
    dec eax

cnt:
    mov edx,0
    mov ebx,10
    div ebx
    add dl,30h
    mov [esi],dl
    dec esi
    loop cnt

    display 4,1,dispnum,8
    display 4,1,end,end_len

exit:
    mov eax,1
    mov ebx,0
    int 80h
