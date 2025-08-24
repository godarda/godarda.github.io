; ----------------------------------------------------------------------------------------------------
; Title          : LISP program for the arithmetic operations using the case statements
; File Name      : gduepzv.lisp
; Compiled       : GNU CLISP 2.49.95+ (2024-11-03) (built on lcy02-amd64-011.buildd [127.0.1.1])
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

(write-line "———————————————————————————————————————————")
(write-line "Program to perform the arithmetic operations ")
(write-line "———————————————————————————————————————————")
(write-line "1.Addition")
(write-line "2.Subtraction")
(write-line "3.Multiplication")
(write-line "4.Division")
(write-line "———————————————————————————————————————————")
(princ "Enter your choice ")
(setq ch(read))
(terpri)(princ "Enter the 1st number ")
(setq a(read))
(terpri)(princ "Enter the 2nd number ")
(setq b(read))
(case ch
(1(format t "~%Addition Of ~d+~d=~d"a b (+ a b)))
(2(format t "~%Subtraction Of ~d-~d=~d"a b (- a b)))
(3(format t "~%Multiplication Of ~d*~d=~d"a b (* a b)))
(4(format t "~%Division Of ~d/~d=~d"a b (/ a b))))
(terpri)(princ "———————————————————————————————————————————")
