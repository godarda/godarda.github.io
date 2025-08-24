; ----------------------------------------------------------------------------------------------------
; Title          : LISP program to perform the arithmetic operations
; File Name      : gdvwwue.lisp
; Compiled       : GNU CLISP 2.49.95+ (2024-11-03) (built on lcy02-amd64-011.buildd [127.0.1.1])
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

(write-line "———————————————————————————————————————————")
(write-line "Program to perform the arithmetic operations")
(write-line "———————————————————————————————————————————")
(format t "Enter the 1st number ")
(setq a(read))
(format t "Enter the 2nd number ")
(setq b(read))
(princ "—————————————————————————")
(format t "~%Addition       | ~d"(+ a b))
(format t "~%Subtraction    | ~d"(- a b))
(format t "~%Multiplication | ~d"(* a b))
(format t "~%Division       | ~d"(/ a b))
(terpri)(format t "———————————————————————————————————————————")
