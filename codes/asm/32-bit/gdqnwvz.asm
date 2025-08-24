; ----------------------------------------------------------------------------------------------------
; Title          : ALP to print the given alphanumeric characters (32-bit)
; File Name      : gdqnwvz.asm
; Compiled       : NASM version 2.16.03
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

section .data
title db "———————————————————————————————————————————"
    db 10, "ALP to print the given alphanumeric characters"
    db 10, "———————————————————————————————————————————",10
title_len equ $-title

input db 10, "Enter characters "
input_len equ $-input

output db 10, "Given characters are "
output_len equ $-output

end db "———————————————————————————————————————————",10
end_len equ $-end

section .bss
num resb 5

section .text
global _start
_start:
    mov eax,4
    mov ebx,1
    mov ecx,title
    mov edx,title_len
    int 80h

    mov eax,4
    mov ebx,1
    mov ecx,input
    mov edx,input_len
    int 80h

    mov eax,3
    mov ebx,2
    mov ecx,num
    mov edx,51
    int 80h

    mov eax,4
    mov ebx,1
    mov ecx,output
    mov edx,output_len
    int 80h
    
    mov eax,4
    mov ebx,1
    mov ecx,num
    mov edx,51
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
