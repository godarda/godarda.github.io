; ----------------------------------------------------------------------------------------------------
; Title          : LISP program to find the min and max of two numbers
; File Name      : gdddysa.lisp
; Compiled       : GNU CLISP 2.49.95+ (2024-11-03) (built on lcy02-amd64-011.buildd [127.0.1.1])
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

(write-line "———————————————————————————————————————————")
(write-line "Program to find the min/max of two numbers")
(write-line "———————————————————————————————————————————")
(princ "Enter the 1st number ")
(setq a(read))
(princ "Enter the 2nd number ")
(setq b(read))
(format t "~%Minimum of ~d OR ~d = ~d"a b (min a b))
(format t "~%Maximum of ~d OR ~d = ~d"a b (max a b))
(terpri)(format t "———————————————————————————————————————————")
