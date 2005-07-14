%include	/usr/lib/rpm/macros.perl
Summary:	A text formatting package based on SGML
Summary(de):	Textformatierungssystem, das vom Linux Documentation Project benutzt wird
Summary(fr):	Système de formattage de texte utilisé par le Linux Documentation Project
Summary(nl):	Tekstformateringssysteem welke door het Linux Documentatie Project wordt gebruikt
Summary(pl):	Narzêdzia konwertuj±ce do linuxdoc-dtd
Summary(tr):	GNU belge biçimlendirme sistemi
Name:		sgml-tools
Version:	1.0.9
Release:	21
License:	Freeware
Group:		Applications/Publishing/SGML
Source0:	http://www.consultronics.com/~cdegroot/sgmltools/dist/%{name}-%{version}.tar.gz
# Source0-md5:	41187c94c4c112253543c50a834c223c
Source1:	sgml2info.1.pl
Source2:	sgml2txt.1.pl
Patch0:		%{name}-%{version}-egcs.patch
Patch1:		%{name}-%{version}-fixsgml2latex.patch
Patch2:		%{name}-%{version}-fixconfigure.patch
Patch3:		%{name}-buildroot.patch
Patch4:		%{name}-manfix.patch
Patch5:		%{name}-datadir.patch
Patch6:		%{name}-sgml-path.patch
Patch7:		%{name}-posix.patch
URL:		http://www.sgmltools.org/
BuildRequires:	autoconf
BuildRequires:	flex
BuildRequires:	groff
BuildRequires:	openjade
BuildRequires:	rpm-perlprov
Requires:	/usr/bin/nsgmls
Requires:	sgmls
Requires:	sgml-common
Obsoletes:	linuxdoc-sgml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGMLtools is a text formatting package based on SGML (Standard
Generalized Markup Language). SGMLtools allows you to produce LaTeX,
HTML, GNU info, LyX, RTF, plain text (via groff), and other format
outputs from a single SGML source. SGMLtools is intended for writing
technical software documentation.

%description -l de
SGMLtools ist ein Textformatierer auf SGML-Basis, der eine Vielzahl
von Ausgabeformaten erzeugen kann. Sie können aus einer einzigen
SGML-Quelldatei PostScript-, dvi- (mit LaTeX), Nur-Text- (mit groff),
HTML- und texinfo-Dateien erstellen.

%description -l fr
SGMLtools est un formatteur de texte basé sur SGML qui vous permet de
produire de nombreux formats de fichiers de sortie. vous pouvez créer
du PostScript et du dvi (avec LaTeX), du texte simple (avec groff), du
HTML, et des fichiers texinfo depuis un simple fichier SGML.

%description -l pl
SGMLtools jest bazuj±cym na SGML (a dok³adniej na LinuxDoc) pakietem
s³u¿±cym do formatowania tekstu. Wchodz±ce w sk³ad pakietu narzêdzia
pozwalaj± na wygenerowanie ze ¼ród³a w SGML dokumentów w formatach
LaTeX, HTML, GNU info, LyX, RTF, tekstowym (przy u¿yciu groff-a).
SGMLtools przeznaczone s± do pisania dokumentacji technicznej
oprogramowania.

%description -l tr
SGMLtools, SGML tabanlý deðiþik biçimlerde çýktýlar üretmenizi
saðlayan bir metin biçimleyicisidir. PostScript, dvi (LaTeX ile), düz
metin (groff ile), HTML dosyalarýný tek bir SGML kaynak dosyasýndan
yaratabilirsiniz.

%description -l nl
SGMLtools is een op SGML gebaseerd tekstverwerkingssyteem waarmee een
aantal verschillende andere bestanden kan worden gemaakt. Uitvoer is
mogelijk in: ASCII, DVI, HTML, LaTeX, PostScript en RTF (Windows help)

%package dtd
Summary:	linuxdoc DTD
Summary(pl):	linuxdoc DTD
Group:		Applications/Publishing/SGML

%description dtd
LinuxDoc DTD.

%description dtd -l pl
LinuxDoc DTD.

%package -n sgmls
Summary:	sgmls
Summary(pl):	sgmls
Version:	1.1
Group:		Applications/Publishing/SGML

%description -n sgmls
sgmls - a validating SGML parser.

%description -n sgmls -l pl
sgmls - parser sprawdzaj±cy poprawno¶æ SGML.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
cd sgmls-1.1
%{__make} config.h \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir}
cd ../entity-map
%{__autoconf}
cd ../iso-entities
%{__autoconf}
cd ..
%{__autoconf}
%configure \
	--with-installed-nsgmls

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man1

%makeinstall \
	libdir=$RPM_BUILD_ROOT%{_datadir}/sgml-tools \
	perl5libdir=$RPM_BUILD_ROOT%{perl_vendorlib}

cd sgmls-1.1
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir}
%{__make} install.man \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir}
cd ..

install sgmls-1.1/sgmls		$RPM_BUILD_ROOT%{_bindir}
install sgmls-1.1/sgmls.pl	$RPM_BUILD_ROOT%{_bindir}
install sgmls-1.1/rast		$RPM_BUILD_ROOT%{_bindir}
install sgmls-1.1/sgmls.man	$RPM_BUILD_ROOT%{_mandir}/man1/sgmls.1
install sgmls-1.1/sgmlsasp.man	$RPM_BUILD_ROOT%{_mandir}/man1/sgmlsasp.1
install sgmls-1.1/rast.man	$RPM_BUILD_ROOT%{_mandir}/man1/rast.1

install %{SOURCE1}	$RPM_BUILD_ROOT%{_mandir}/pl/man1/sgml2info.1
install %{SOURCE2}	$RPM_BUILD_ROOT%{_mandir}/pl/man1/sgml2txt.1

install -d $RPM_BUILD_ROOT%{_datadir}/sgml/sgml-tools
install $RPM_BUILD_ROOT%{_datadir}/sgml-tools/dtd/* $RPM_BUILD_ROOT%{_datadir}/sgml/sgml-tools

find $RPM_BUILD_ROOT%{_bindir} -type f -o -type l | \
	grep -v nsgmls | sed "s|$RPM_BUILD_ROOT||g" > file.list

cat > doc/COPYRIGHT <<EOF
(C) International Organization for Standardization 1986
Permission to copy in any form is granted for use with
conforming SGML systems and applications as defined in
ISO 8879, provided this notice is included in all copies.
EOF

rm -rf $RPM_BUILD_ROOT%{_datadir}/sgml/iso-entities-8879.1986

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -L %{_libdir}/sgml-tools/dtd/sgml-tools ]; then
	rm -f %{_libdir}/sgml-tools/dtd/sgml-tools
fi
if [ -L %{_datadir}/sgml-tools/dtd/sgml-tools ]; then
	rm -f %{_datadir}/sgml-tools/dtd/sgml-tools
fi

%files
%defattr(644,root,root,755)
%doc doc/{html,guide*,example*,Makedoc.sh,README}
%{_datadir}/sgml-tools
%{perl_vendorlib}/Text/EntityMap.pm
%attr(755,root,root) %{_bindir}/rtf2rtf
%attr(755,root,root) %{_bindir}/sgmlpre
%attr(755,root,root) %{_bindir}/sgml2*
%attr(755,root,root) %{_bindir}/sgmltools.v1
%attr(755,root,root) %{_bindir}/sgmlcheck

%{_mandir}/man1/sgml2*.1*
%{_mandir}/man1/sgmlcheck.1*
%{_mandir}/man1/sgmltools.1*
%lang(pl) %{_mandir}/pl/man1/sgml2*.1*

%files -n sgmls
%defattr(644,root,root,755)
%doc sgmls-1.1/LICENSE sgmls-1.1/NEWS
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
%{_datadir}/entity-map
