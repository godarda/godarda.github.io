; ----------------------------------------------------------------------------------------------------
; Title          : LISP program to perform the bitwise operations
; File Name      : gdmalgp.lisp
; Compiled       : GNU CLISP 2.49.95+ (2024-11-03) (built on lcy02-amd64-011.buildd [127.0.1.1])
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

(write-line "———————————————————————————————————————————")
(write-line "Program to perform the bitwise operations")
(write-line "———————————————————————————————————————————")
(princ "Enter the 1st number ")
(setq a(read))
(princ "Enter the 2nd number ")
(setq b(read))
(format t "~%~d AND ~d           | ~d"a b(logand a b))
(format t "~%~d NAND ~d          | ~d"a b(lognand a b))
(format t "~%~d INCLUSIVE OR ~d  | ~d"a b(logior a b))
(format t "~%~d EXCLUSIVE OR ~d  | ~d"a b(logxor a b))
(format t "~%~d NOT ~d           | ~d"a b(lognor a b))
(format t "~%~d EQUIVALANCE ~d   | ~d"a b(logeqv a b))
(terpri)(format t "———————————————————————————————————————————")
