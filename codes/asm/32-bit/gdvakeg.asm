; ----------------------------------------------------------------------------------------------------
; Title          : ALP to identify the Central Processing Unit (CPU) type (32-bit)
; File Name      : gdvakeg.asm
; Compiled       : NASM version 2.16.03
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

section .data
title db "———————————————————————————————————————————"
    db 10, "ALP to identify the Central Processing Unit type"
    db 10, "———————————————————————————————————————————"
title_len equ $-title

output db 10,10,"The CPU type is "
output_len equ $-output

end db "———————————————————————————————————————————",10
end_len equ $-end

section .bss
    var1 resd 1
    var2 resd 1
    var3 resd 1
    var4 resb 49

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
    CPUID
    mov [var1],ebx
    mov [var2],edx
    mov [var3],ecx
    display 4,1,title,title_len
    display 4,1,output,output_len
    display 4,1,var1,4
    display 4,1,var2,4
    display 4,1,var3,4

    mov edi,var4
    mov eax,80000002h
    cpuid
    call CPU_PROC

    mov eax,80000003h
    cpuid
    call CPU_PROC

    mov eax, 80000004h
    cpuid
    call CPU_PROC
    mov al,10
    stosb

    display 4,1,var4,49
    display 4,1,end,end_len

    mov eax,1
    mov ebx,0
    int 80h

CPU_PROC:
    stosd
    mov eax,ebx
    stosd
    mov eax,ecx
    stosd
    mov eax,edx
    stosd
    ret
