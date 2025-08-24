; ----------------------------------------------------------------------------------------------------
; Title          : LISP program for the positive-negative test of a given number
; File Name      : gdkdena.lisp
; Compiled       : GNU CLISP 2.49.95+ (2024-11-03) (built on lcy02-amd64-011.buildd [127.0.1.1])
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

(write-line "———————————————————————————————————————————")
(write-line "Program to check a number is +ve or -ve")
(write-line "———————————————————————————————————————————")
(princ "Enter the number ")
(setq a(read))
(if(= a 0)
(format t "~%~d is neither +ve nor -ve "a))
(if(> a 0)
(format t "~%~d is +ve number "a))
(if(< a 0)
(format t "~%~d is -ve number "a))
(terpri)(format t "———————————————————————————————————————————")
