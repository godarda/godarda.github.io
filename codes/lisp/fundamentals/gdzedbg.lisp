; ----------------------------------------------------------------------------------------------------
; Title          : LISP program to demonstrate the use of trigonometric functions
; File Name      : gdzedbg.lisp
; Compiled       : GNU CLISP 2.49.95+ (2024-11-03) (built on lcy02-amd64-011.buildd [127.0.1.1])
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

(write-line "———————————————————————————————————————————")
(write-line "Program for trigonometric functions")
(write-line "———————————————————————————————————————————")
(princ "Enter the angle ")
(setq a(read))
(format t "~%  sin(~d) | ~d"a (sin a))
(format t "~%  cos(~d) | ~d"a (cos a))
(format t "~%  tan(~d) | ~d"a (tan a))
(format t "~%  cot(~d) | ~d"a (/ (cos 45) (sin 45)))
(format t "~%  sec(~d) | ~d"a (/ 1 (cos 45)))
(format t "~%cosec(~d) | ~d"a (/ 1 (sin 45)))
(terpri)(format t "———————————————————————————————————————————")
