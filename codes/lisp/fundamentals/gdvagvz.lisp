; ----------------------------------------------------------------------------------------------------
; Title          : LISP program to demonstrate the use of numeric conversion functions
; File Name      : gdvagvz.lisp
; Compiled       : GNU CLISP 2.49.95+ (2024-11-03) (built on lcy02-amd64-011.buildd [127.0.1.1])
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

(write-line "———————————————————————————————————————————")
(write-line "Program to use numeric functions")
(write-line "———————————————————————————————————————————")
(terpri)(princ (floor 15 2))
(terpri)(princ (ceiling 15 2))
(terpri)(princ (round 15 2))
(terpri)(princ (truncate 15 2))
(terpri)(princ (ffloor 15 2))
(terpri)(princ (fceiling 15 2))
(terpri)(princ (fround 15 2))
(terpri)(princ (ftruncate 15 2))
(terpri)(princ (mod 15 2))
(terpri)(princ (complex 2 15))
(terpri)(setq c(complex 15 2))
(write c)
(terpri)(princ (realpart c))
(terpri)(princ (imagpart c))
(terpri)(format t "———————————————————————————————————————————")
