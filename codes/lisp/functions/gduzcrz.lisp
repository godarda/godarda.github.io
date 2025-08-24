; ----------------------------------------------------------------------------------------------------
; Title          : LISP program to find the area of a circle using a function
; File Name      : gduzcrz.lisp
; Compiled       : GNU CLISP 2.49.95+ (2024-11-03) (built on lcy02-amd64-011.buildd [127.0.1.1])
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

(write-line "———————————————————————————————————————————")
(write-line "Program to find the area of a circle")
(write-line "———————————————————————————————————————————")
(princ "Enter the radius ")
(setq r(read))
(defconstant PI 3.1416)
(defun Area()
(setq A(* PI r r))
(terpri)(princ "The area of a circle is ")
(write A)
(setq C(* 6.2831 r))
(terpri)(princ "The circumference of a circle is ")
(write C))
(Area)
(terpri)(format t "———————————————————————————————————————————")
