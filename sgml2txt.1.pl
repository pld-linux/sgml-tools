.\" {PTM/WK/2000-VI}
.\" Process this file with
.\" groff -man -Tascii sgml2txt.1
.\"
.TH SGML2TXT 1 "10 listopada 1997"
.SH NAZWA
sgml2txt \- tw�rz zwyk�y tekst z pliku �r�d�owego SGML
.SH SK�ADNIA
.B sgml2txt
.RB [ opcja-og�lna ...]
.RB [ --man ]
.RB [ --filter ]
.IR plik [\fB.sgml\fP]
.SH OPIS
.B sgml2txt
konwertuje plik �r�d�owy SGML na wyj�cie w ASCII lub ISO-8859-1.
Wynik pojawi si� w
.IR plik.txt ,
gdzie
.I plik
jest nazw� pliku �r�d�owego SGML.
.LP
Do ustawie� warunkowych (conditionals) ustawiana jest para atrybut/warto��
"output=txt".
.SH OPCJE
.B sgml2info
przyjmuje wszystkie opcje og�lne opisane w
.B sgmltools (1)
oraz nast�puj�ce opcje charakterystyczne:
.TP
.BR --man ", " -m
Daje w wyniku plik �r�d�owy groff, odpowiedni do utworzenia przez
.B groff -man
sformatowanych stron podr�cznika systemowego man.
.TP
.BR --filter ", " -f
Usuwa z postaci po�redniej utworzonej przez
.BR groff (1)
nadpisania wykonane z u�yciem backspace.
.TP
.BR --pass ", " -P
Argument opcji pass (przeka�) dodawany jest do opcji wiersza polece�
obs�ugiwanej przez
.BR groff (1).
.IP plik
okre�la plik �r�d�owy SGML, o nazwie albo
.I plik
albo
.I plik.sgml
.SH PLIKI
Wykorzystywanych jest wiele plik�w z
.B $LINUXDOCLIB
i
.BR $LINUXDOCBIN .
.SH B��DY
Nie znaleziono.
.SH AUTOR
Greg Hankins <greg.hankins@cc.gatech.edu>, w oparciu o skrypty
Toma Gordona i Alexandra Horza.
Napisane ponownie przez Cees de Groot <cg@pobox.com>.
.SH "ZOBACZ TAK�E"
.BR sgmltools (1),
.BR sgml2html (1),
.BR sgml2info (1),
.BR sgml2latex (1),
.BR sgml2lyx (1),
.BR sgml2rtf (1),
.BR sgmlcheck (1).
