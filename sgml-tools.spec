Summary:	Text formatting system used by the Linux Documentation Project
Summary(de):	Textformatierungssystem, das vom Linux Documentation Project benutzt wird
Summary(fr):	Système de formattage de texte utilisé par le Linux Documentation Project.
Summary(nl):	Tekstformateringssysteem welke door het Linux Documentatie Project wordt gebruikt.
Summary(pl):	Narzêdzia konweruj±ce do linuxdoc-dtd 
Summary(tr):	GNU belge biçimlendirme sistemi
Name:		sgml-tools
Version:	1.0.7
Release:	6
Copyright:	freeware
Group:		Applications/Publishing/SGML
Group(pl):	Aplikacje/Publikowanie/SGML
Source:		http://ftp.nllgg.nl/pub2/SGMLtools/1.0/%{name}-%{version}.tar.gz
Patch0:		%{name}.patch
Patch1:		%{name}-no-doc-rebuild.patch
URL:		http://www.nllgg.nl/SGMLtools
Obsoletes:	linuxdoc-sgml
BuildRequires:	openjade
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGMLtools is a SGML-based text formatter which allows you to
produce a variety of output formats. You can create PostScript and
dvi (with LaTeX), plain text (with groff), HTML, and texinfo files
from a single SGML source file.

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
Narzêdzia konwertuj±ce dla linuxdoc-dtd.

%description -l tr
SGMLtools, SGML tabanlý deðiþik biçimlerde çýktýlar üretmenizi saðlayan bir
metin biçimleyicisidir. PostScript, dvi (LaTeX ile), düz metin (groff ile),
HTML dosyalarýný tek bir SGML kaynak dosyasýndan yaratabilirsiniz.

%description -l nl
SGMLtools is een op SGML gebaseerd tekstverwerkingssyteem waarmee een
aantal verschillende andere bestanden kan worden gemaakt. Uitvoer is
mogelijk in: ASCII, DVI, HTML, LaTeX, PostScript en RTF (Windows help)

%package dtd 
Summary:	linuxdoc DTD
Summary(pl):	linuxdoc DTD
Group:		Applications/Publishing/SGML
Group(pl):	Aplikacje/Publikowanie/SGML

%description dtd
Linuxdoc DTD.

%description -l pl dtd
Linuxdoc DTD.

%package -n  sgmls
Summary:	sgmls
Summary(pl):	sgmls
Version:	1.1
Group:		Applications/Publishing/SGML
Group(pl):	Aplikacje/Publikowanie/SGML

%description -n sgmls
Sgmls

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--with-installed-nsgmls

%{__make} OPTIMIZE="$RPM_OPT_FLAGS"

cd sgmls-1.1 
%{__make} OPTIMIZE="$RPM_OPT_FLAGS" PREFIX=$RPM_BUILD_ROOT%{_prefix}
%{__make} install 
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT/%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

install sgmls-1.1/sgmls		$RPM_BUILD_ROOT%{_bindir}
install sgmls-1.1/sgmls.pl	$RPM_BUILD_ROOT%{_bindir}
install sgmls-1.1/rast		$RPM_BUILD_ROOT%{_bindir}
install sgmls-1.1/sgmls.man	$RPM_BUILD_ROOT%{_mandir}/man1/sgmls.1
install sgmls-1.1/sgmlsasp.man	$RPM_BUILD_ROOT%{_mandir}/man1/sgmlsasp.1
install sgmls-1.1/rast.man	$RPM_BUILD_ROOT%{_mandir}/man1/rast.1

strip $RPM_BUILD_ROOT%{_bindir}/* || :

install -d $RPM_BUILD_ROOT%{_datadir}/sgml/sgml-tools
install $RPM_BUILD_ROOT%{_libdir}/sgml-tools/dtd/* $RPM_BUILD_ROOT%{_datadir}/sgml/sgml-tools 

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	sgmls-1.1/LICENSE sgmls-1.1/NEWS 

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
%doc %dir /usr/doc/sgml-tools
%doc /usr/doc/sgml-tools/*
%{_libdir}/sgml
%{_libdir}/sgml-tools
%{_libdir}/perl5/Text/EntityMap.pm
%attr(755,root,root) %{_bindir}/rtf2rtf
%attr(755,root,root) %{_bindir}/sgmlpre
%attr(755,root,root) %{_bindir}/sgml2* 
%attr(755,root,root) %{_bindir}/sgmltools 
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
