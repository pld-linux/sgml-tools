Summary:     text formatting system used by the Linux Documentation Project
%define      packagename sgml-tools
%define      packver 1.0.7
Name:        %{packagename}
Obsoletes:   linuxdoc-sgml
Version:     %{packver}
Release:     4d
Copyright:   freeware
Group:       Utilities/Text/SGML
Source:      http://ftp.nllgg.nl/pub2/SGMLtools/1.0/%{name}-%{version}.tar.gz
Url:         http://www.nllgg.nl/SGMLtools
Patch:       %{name}.patch
Buildroot:   /tmp/%{name}-%{version}-%{release}-root
Summary(de): Textformatierungssystem, das vom Linux Documentation Project benutzt wird
Summary(fr): Syst�me de formattage de texte utilis� par le Linux Documentation Project.
Summary(tr): GNU belge bi�imlendirme sistemi
Summary(nl): Tekstformateringssysteem welke door het Linux Documentatie Project wordt gebruikt.
Summary(pl): Narz�dzia konweruj�ce do linuxdoc-dtd 

%description
SGMLtools is a SGML-based text formatter which allows you to
produce a variety of output formats. You can create PostScript and
dvi (with LaTeX), plain text (with groff), HTML, and texinfo files
from a single SGML source file.

%description -l pl
Narz�dzia konweruj�ce do linuxdoc-dtd 

%description -l de
SGMLtools ist ein Textformatierer auf SGML-Basis, der eine Vielzahl
von Ausgabeformaten erzeugen kann. Sie k�nnen aus einer einzigen 
SGML-Quelldatei PostScript-, dvi- (mit LaTeX), Nur-Text- 
(mit groff), HTML- und texinfo-Dateien erstellen.

%description -l fr
SGMLtools est un formatteur de texte bas� sur SGML qui vous permet
de produire de nombreux formats de fichiers de sortie. vous pouvez
cr�er du PostScript et du dvi (avec LaTeX), du texte simple (avec groff),
du HTML, et des fichiers texinfo depuis un simple fichier SGML.

%description -l tr
SGMLtools, SGML tabanl� de�i�ik bi�imlerde ��kt�lar �retmenizi sa�layan bir
metin bi�imleyicisidir. PostScript, dvi (LaTeX ile), d�z metin (groff ile),
HTML dosyalar�n� tek bir SGML kaynak dosyas�ndan yaratabilirsiniz.

%description -l nl
SGMLtools is een op SGML gebaseerd tekstverwerkingssyteem waarmee een
aantal verschillende andere bestanden kan worden gemaakt. Uitvoer is
mogelijk in: ASCII, DVI, HTML, LaTeX, PostScript en RTF (Windows help)

%package dtd 
Summary:     linuxdoc DTD
Group:       Utilities/Text/SGML
Summary(pl): linuxdoc DTD

%description dtd
Linuxdoc DTD

%description -l pl dtd
Linuxdoc DTD

%package -n  sgmls
Summary:     sgmls
version:     1.1
Group:       Utilities/Text/SGML
Summary(pl): sgmls

%description -n sgmls
Sgmls

%description -n sgmls
Sgmls

%prep
%setup -q
%patch -p1

%build
CFLAGS=$RPM_OPT_FLAGS \
./configure --prefix=/usr --with-installed-nsgmls 

make OPTIMIZE="$RPM_OPT_FLAGS"

cd sgmls-1.1 
make OPTIMIZE="$RPM_OPT_FLAGS" PREFIX=$RPM_BUILD_ROOT/usr
make install 
cd ..

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/sgmls $RPM_BUILD_ROOT/usr/bin
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/sgmls.pl $RPM_BUILD_ROOT/usr/bin/
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/rast $RPM_BUILD_ROOT/usr/bin
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/sgmls.man $RPM_BUILD_ROOT/usr/man/man1/sgmls.1
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/sgmlsasp.man $RPM_BUILD_ROOT/usr/man/man1/sgmlsasp.1
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/rast.man $RPM_BUILD_ROOT/usr/man/man1/rast.1

strip $RPM_BUILD_ROOT/usr/bin/rast
strip $RPM_BUILD_ROOT/usr/bin/sgmls
strip $RPM_BUILD_ROOT/usr/bin/rtf2rtf
strip $RPM_BUILD_ROOT/usr/bin/sgmlsasp 
strip $RPM_BUILD_ROOT/usr/bin/sgmlpre

install -d $RPM_BUILD_ROOT/usr/share/sgml/sgml-tools
install $RPM_BUILD_ROOT/usr/lib/sgml-tools/dtd/* $RPM_BUILD_ROOT/usr/share/sgml/sgml-tools 

bzip2 -9 $RPM_BUILD_ROOT/usr/man/man1/*

%post 
#!/bin/bash 
pushd `pwd` 
cd /usr/lib/sgml-tools
ln -f -s -n ../../share/sgml/sgml-tools/ dtd
popd 

%preun 
#!/bin/bash
if [ -L /usr/lib/sgml-tools/dtd ]; then
rm -rf /usr/lib/sgml-tools/dtd
if  

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/usr/lib/sgml-tools
/usr/lib/perl5/Text/EntityMap.pm
/usr/lib/sgml
/usr/doc/sgml-tools
%attr(711,root,root) /usr/bin/rtf2rtf
%attr(711,root,root) /usr/bin/sgmlpre
%attr(755,root,root) /usr/bin/sgml2* 
%attr(755,root,root) /usr/bin/sgmltools 
%attr(755,root,root) /usr/bin/sgmlcheck

%attr(644,root, man) /usr/man/man1/sgml2*.1.bz2
%attr(644,root, man) /usr/man/man1/sgmlcheck.1.bz2
%attr(644,root, man) /usr/man/man1/sgmltools.1.bz2

%files -n sgmls 
%defattr(644,root,root,755)
%doc sgmls-1.1/LICENSE sgmls-1.1/NEWS 
%attr(711,root,root) /usr/bin/rast
%attr(711,root,root) /usr/bin/sgmls
%attr(711,root,root) /usr/bin/sgmlsasp 
%attr(755,root,root) /usr/bin/sgmls.pl 

%attr(644,root, man) /usr/man/man1/rast.1.bz2
%attr(644,root, man) /usr/man/man1/sgmls.1.bz2
%attr(644,root, man) /usr/man/man1/sgmlsasp.1.bz2

%files dtd
%defattr(644,root,root,755)
/usr/share/sgml/sgml-tools
/usr/lib/entity-map
