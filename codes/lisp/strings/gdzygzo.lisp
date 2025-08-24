; ----------------------------------------------------------------------------------------------------
; Title          : LISP program to check whether a given string is a palindrome
; File Name      : gdzygzo.lisp
; Compiled       : GNU CLISP 2.49.95+ (2024-11-03) (built on lcy02-amd64-011.buildd [127.0.1.1])
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

(write-line "———————————————————————————————————————————")
(write-line "Program to check whether string is palindrome")
(write-line "———————————————————————————————————————————")
(princ "Enter the string ")
(setq s(string(read)))
(setq s1(string s))
(setq s2(reverse s1))
(if (string-equal s1 s2)
(format t "~%~d is palindrome"s1))
(if (string-not-equal s1 s2)
(format t "~%~d is not palindrome"s1))
(terpri)(princ "———————————————————————————————————————————")
