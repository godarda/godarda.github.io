; ----------------------------------------------------------------------------------------------------
; Title          : LISP program to print the even and odd numbers
; File Name      : gdzzzay.lisp
; Compiled       : GNU CLISP 2.49.95+ (2024-11-03) (built on lcy02-amd64-011.buildd [127.0.1.1])
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

(write-line "———————————————————————————————————————————")
(write-line "Program to print the even and odd numbers")
(write-line "———————————————————————————————————————————")
(setq a 0)
(princ a)
(loop
(setq a(+ a 2))
(terpri)(princ a)
(when(>= a 10)(return a)))

(terpri)(terpri)
(setq a 1)
(write a)(terpri)
(loop
(setq a(+ a 2))
(when(> a 10)(return a))
(princ a)(terpri))
(format t "———————————————————————————————————————————")
