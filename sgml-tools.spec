Summary: 	A text formatting package based on SGML.
Summary(de):    Textformatierungssystem, das vom Linux Documentation Project benutzt wird
Summary(fr):    Système de formattage de texte utilisé par le Linux Documentation Project.
Summary(nl):    Tekstformateringssysteem welke door het Linux Documentatie Project wordt gebruikt.
Summary(pl):    Narzêdzia konweruj±ce do linuxdoc-dtd
Summary(tr):    GNU belge biçimlendirme sistemi
Name: 		sgml-tools
Version: 	1.0.9
Release: 	9
Copyright: 	freeware  
Group: 		Applications/Publishing/SGML
Group(pl):	Aplikacje/Publikowanie/SGML
Source: 	http://www.consultronics.com/~cdegroot/sgmltools/dist/%{name}-%{version}.tar.gz
Patch0: 	%{name}-%{version}-egcs.patch
Patch1: 	%{name}-%{version}-fixsgml2latex.patch
Patch2: 	%{name}-%{version}-fixconfigure.patch
Patch3: 	%{name}-buildroot.patch
Patch4: 	%{name}-manfix.patch
Patch5:		%{name}-%{version}-jtz.patch
URL:            http://www.sgmltools.org
Requires:       /usr/bin/nsgmls
Obsoletes:      linuxdoc-sgml
BuildRequires: 	openjade
Buildroot: 	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGMLtools is a text formatting package based on SGML (Standard
Generalized Markup Language).  SGMLtools allows you to produce LaTeX,
HTML, GNU info, LyX, RTF, plain text (via groff), and other format
outputs from a single SGML source.  SGMLtools is intended for writing
technical software documentation.

%description -l de
SGMLtools ist ein Textformatierer auf SGML-Basis, der eine Vielzahl
von Ausgabeformaten erzeugen kann. Sie können aus einer einzigen
SGML-Quelldatei PostScript-, dvi- (mit LaTeX), Nur-Text-
(mit groff), HTML- und texinfo-Dateien erstellen.

%description -l fr
SGMLtools est un formatteur de texte basé sur SGML qui vous permet
de produire de nombreux formats de fichiers de sortie. vous pouvez
créer du PostScript et du dvi (avec LaTeX), du texte simple (avec groff),
du HTML, et des fichiers texinfo depuis un simple fichier SGML.

%description -l pl
SGMLtools jest bazuj±cym na SGML (a dok³adniej na LinuxDoc) pakietem 
s³u¿±cym do formatowania tekstu. Wchodz±ce w sk³ad pakietu narzêdzia 
pozwalaj± na wygenerowanie ze ¼ród³a w SGML dokumentów w formatach 
LaTeX, HTML, GNU info, LyX, RTF, tekstowym (przy u¿yciu groff-a).
SGMLtools przeznaczone s± do pisania dokumentacji technicznej 
oprogramowania.

%description -l tr
SGMLtools, SGML tabanlý deðiþik biçimlerde çýktýlar üretmenizi saðlayan bir
metin biçimleyicisidir. PostScript, dvi (LaTeX ile), düz metin (groff ile),
HTML dosyalarýný tek bir SGML kaynak dosyasýndan yaratabilirsiniz.

%description -l nl
SGMLtools is een op SGML gebaseerd tekstverwerkingssyteem waarmee een
aantal verschillende andere bestanden kan worden gemaakt. Uitvoer is
mogelijk in: ASCII, DVI, HTML, LaTeX, PostScript en RTF (Windows help)

%package dtd
Summary:        linuxdoc DTD
Summary(pl):    linuxdoc DTD
Group:          Applications/Publishing/SGML
Group(pl):      Aplikacje/Publikowanie/SGML

%description dtd
LinuxDoc DTD.

%description -l pl dtd
LinuxDoc DTD.

%package -n  sgmls
Summary:        sgmls
Summary(pl):    sgmls
Version:        1.1
Group:          Applications/Publishing/SGML
Group(pl):      Aplikacje/Publikowanie/SGML

%description -n sgmls
sgmls - a validating SGML parser

%prep
%setup -q
%patch0 -p1 -b .egcs
%patch1 -p1 -b .fixsgml2latex
%patch2 -p1 -b .fixconfigure
%patch3 -p1 -b .buildroot
%patch4 -p1 -b .manfix
%patch5 -p1 -b .jtz

%build
cd sgmls-1.1
	%{__make} config.h \
		 prefix=$RPM_BUILD_ROOT/%{_prefix} \
		 mandir=$RPM_BUILD_ROOT%{_mandir}
	%{__make} CFLAGS="$RPM_OPT_FLAGS" \
                 prefix=$RPM_BUILD_ROOT/%{_prefix} \
                 mandir=$RPM_BUILD_ROOT%{_mandir}
cd ..

%configure \
	--with-installed-nsgmls \
	--libdir=$RPM_BUILD_ROOT/usr/lib/sgml-tools \
	--datadir=$RPM_BUILD_ROOT/usr/lib
  
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall libdir=$RPM_BUILD_ROOT/usr/lib/sgml-tools \
       datadir=$RPM_BUILD_ROOT/usr/lib

cd sgmls-1.1
	%{__make} install \
                 prefix=$RPM_BUILD_ROOT/%{_prefix} \
                 mandir=$RPM_BUILD_ROOT%{_mandir}
	%{__make} install.man \
                 prefix=$RPM_BUILD_ROOT/%{_prefix} \
                 mandir=$RPM_BUILD_ROOT%{_mandir}
cd ..

install sgmls-1.1/sgmls         $RPM_BUILD_ROOT%{_bindir}
install sgmls-1.1/sgmls.pl      $RPM_BUILD_ROOT%{_bindir}
install sgmls-1.1/rast          $RPM_BUILD_ROOT%{_bindir}
install sgmls-1.1/sgmls.man     $RPM_BUILD_ROOT%{_mandir}/man1/sgmls.1
install sgmls-1.1/sgmlsasp.man  $RPM_BUILD_ROOT%{_mandir}/man1/sgmlsasp.1
install sgmls-1.1/rast.man      $RPM_BUILD_ROOT%{_mandir}/man1/rast.1

strip $RPM_BUILD_ROOT%{_bindir}/* || :

install -d $RPM_BUILD_ROOT%{_datadir}/sgml/sgml-tools
install $RPM_BUILD_ROOT%{_libdir}/sgml-tools/dtd/* $RPM_BUILD_ROOT%{_datadir}/sgml/sgml-tools

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
        sgmls-1.1/LICENSE sgmls-1.1/NEWS

find $RPM_BUILD_ROOT/usr/bin -type f -o -type l | \
	grep -v nsgmls | sed "s|$RPM_BUILD_ROOT||g" > file.list

cat > doc/COPYRIGHT <<EOF
(C) International Organization for Standardization 1986
Permission to copy in any form is granted for use with
conforming SGML systems and applications as defined in
ISO 8879, provided this notice is included in all copies.
EOF

%post
cd /usr/lib/sgml-tools
ln -f -s -n ../../share/sgml/sgml-tools/ dtd

%preun
if [ -L /usr/lib/sgml-tools/dtd ]; then
        rm -rf /usr/lib/sgml-tools/dtd
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{html,guide*,example*,Makedoc.sh,README}
%{_libdir}/sgml
%{_libdir}/sgml-tools
%{_libdir}/perl5/Text/EntityMap.pm
%attr(755,root,root) %{_bindir}/rtf2rtf
%attr(755,root,root) %{_bindir}/sgmlpre
%attr(755,root,root) %{_bindir}/sgml2*
%attr(755,root,root) %{_bindir}/sgmltools.v1
%attr(755,root,root) %{_bindir}/sgmlcheck

%{_mandir}/man1/sgml2*.1*
%{_mandir}/man1/sgmlcheck.1*
%{_mandir}/man1/sgmltools.1*

%files -n sgmls
%defattr(644,root,root,755)
%doc sgmls-1.1/LICENSE.gz sgmls-1.1/NEWS.gz
%attr(755,root,root) %{_bindir}/rast
%attr(755,root,root) %{_bindir}/sgmls
%attr(755,root,root) %{_bindir}/sgmlsasp
%attr(755,root,root) %{_bindir}/sgmls.pl

%{_mandir}/man1/rast.1*
%{_mandir}/man1/sgmls.1*
%{_mandir}/man1/sgmlsasp.1*

%files dtd
%defattr(644,root,root,755)
%{_datadir}/sgml/sgml-tools
%{_libdir}/entity-map
