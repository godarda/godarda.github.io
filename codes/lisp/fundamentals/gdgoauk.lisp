; ----------------------------------------------------------------------------------------------------
; Title          : LISP program to swap the given numbers
; File Name      : gdgoauk.lisp
; Compiled       : GNU CLISP 2.49.95+ (2024-11-03) (built on lcy02-amd64-011.buildd [127.0.1.1])
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

(write-line "———————————————————————————————————————————")
(write-line "Program to swap the given numbers")
(write-line "———————————————————————————————————————————")
(princ "Enter the 1st number a=")
(setq a(read))
(princ "Enter the 2nd number b=")
(setq b(read))
(write-line "After swapping...")
(setq a(+ a b))
(setq b(- a b))
(setq a(- a b))
(terpri)(princ "a=")(write a)
(terpri)(princ "b=")(write b)
(terpri)(format t "———————————————————————————————————————————")
