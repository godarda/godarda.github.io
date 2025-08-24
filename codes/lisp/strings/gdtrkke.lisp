; ----------------------------------------------------------------------------------------------------
; Title          : LISP program to perform the string operations
; File Name      : gdtrkke.lisp
; Compiled       : GNU CLISP 2.49.95+ (2024-11-03) (built on lcy02-amd64-011.buildd [127.0.1.1])
; Author         : GoDarda
; License        : GNU General Public License
; ----------------------------------------------------------------------------------------------------

(write-line "———————————————————————————————————————————")
(write-line "Program to perform the string operations ")
(write-line "———————————————————————————————————————————")
(princ "Enter the 1st string ")
(setq s1(string(read)))
(princ "Enter the 2nd string ")
(setq s2(string(read)))
(format t "~%Entered S1 S2  | ~d ~d"s1 s2)
(format t "~%Reverse S1 S2  | ~d ~d"(reverse s1) (reverse s2))
(format t "~%Length  S1 S2  | ~d ~d"(length s1) (length s2))
(format t "~%Uppercase S1   | ~d ~d"(string-upcase s1) (string-upcase s2))
(format t "~%Lowercase S1   | ~d ~d"(string-downcase s1) (string-downcase s2))
(format t "~%Togalcase S1   | ~d ~d"(string-capitalize s1) (string-capitalize s2))
(format t "~%Concatination  | ~d "(concatenate 'string s1 s2))
(format t "~%Comparision    | ~d "(string-equal s1 s2)) ;CS-case sensitive
(format t "~%Subsequence 0  | ~d ~d"(subseq s1 0) (subseq s2 0))
(format t "~%Character at 0 | ~d ~d"(char s1 0) (char s2 0))
(terpri)(princ "———————————————————————————————————————————")
