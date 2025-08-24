; ----------------------------------------------------------------------------------------------------
; Title          : ALP to convert the Binary Coded Decimal (BCD) to hexadecimal number (64-bit)
; File Name      : gdvthab.asm
; Compiled       : NASM version 2.16.03
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

section .data
title db "———————————————————————————————————————————"
    db 10, "ALP to convert the BCD to hexadecimal number"
    db 10, "———————————————————————————————————————————"
    db 10, "Enter 5 digit BCD number "
title_len equ $-title

output db 10, "Hexadecimal equivalent is "
output_len equ $-output

end db 10, "———————————————————————————————————————————",10
end_len equ $-end

section .bss
    numascii resb 06   
    opbuff resb 05
    dnumbuff resb 08

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
bcd2hex_proc:
    display 1,1,title,title_len
    display 0,0,numascii,6
    display 1,1,output,output_len
    mov rsi,numascii
    mov rcx,05
    mov rax,0
    mov rbx,0ah

b2hup1:    
    mov rdx,0
    mul rbx
    mov dl,[rsi]
    sub dl,30h
    add rax,rdx
    inc rsi
    loop b2hup1
    mov rbx,rax
    call disp32_num
    call exit
    ret

disp32_num:
    mov rdi,dnumbuff        
    mov rcx,08            

dispup1:
    rol ebx,4            
    mov dl,bl            
    and dl,0fh            
    add dl,30h            
    cmp dl,39h            
    jbe dispskip1    
    add dl,07h        

dispskip1:
    mov [rdi],dl        
    inc rdi        
    loop dispup1        
    display 1,1,dnumbuff+3,5
    ret

exit:
    display 1,1,end,end_len
    mov rax,60
    mov rdi,0
    syscall
