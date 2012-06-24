.\" {PTM/WK/2000-VI}
.\" Process this file with
.\" groff -man -Tascii sgml2info.1
.\"
.TH SGML2INFO 1 "10 listopada 1997"
.SH NAZWA
sgml2info \- tw�rz wyj�cie GNU info z pliku �r�d�owego SGML
.SH SK�ADNIA
.B sgml2info
.RB [ opcja og�lna ...]
.IR plik [\fB.sgml\fP]
.SH OPIS
.B sgml2info
konwertuje plik �r�d�owy z formatu SGML na format GNU info.
Wynik pojawi si� w
.IR plik.info ,
gdzie
.I plik
jest nazw� pliku �r�d�owego SGML.
.LP
Do ustawie� warunkowych (conditionals) ustawiana jest para atrybut/warto��
"output=info".
.SH OPCJE
.B sgml2info
przyjmuje wszystkie opcje og�lne opisane w
.BR sgmltools (1).
.IP plik
okre�la plik �r�d�owy SGML, o nazwie albo
.I plik
albo
.I plik.sgml
.SH PLIKI
Wykorzystywanych jest wiele plik�w z
.BR $LINUXDOCLIB .
.SH AUTOR
Christian Schwarz <schwarz@monet.m.isar.de>,
Greg Hankins <greg.hankins@cc.gatech.edu>,
Cees de Groot <cg@pobox.com>.
.SH "ZOBACZ TAK�E"
.BR sgmltools (1),
.BR sgml2html (1),
.BR sgml2latex (1), 
.BR sgml2lyx (1), 
.BR sgml2rtf (1), 
.BR sgml2txt (1),
.BR sgmlcheck (1). 
