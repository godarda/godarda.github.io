; ----------------------------------------------------------------------------------------------------
; Title          : LISP program to calculate the square and cube of numbers
; File Name      : gdiewcv.lisp
; Compiled       : GNU CLISP 2.49.95+ (2024-11-03) (built on lcy02-amd64-011.buildd [127.0.1.1])
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

(write-line "+--------+---------+------------+")
(write-line "|Numbers | Squares | Cubes      |")
(write-line "+--------+---------+------------+")
(dotimes(n 11)
(format t "   ~d         ~d          ~d       ~%"n(* n n)(* n(* n n))))
(write-line "+--------+---------+------------+")
