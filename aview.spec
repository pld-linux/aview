Summary:	ASCII-Art image browser and animation player
Summary(pl):	Przegl±darka obrazków i animacji jako ASCII Art
Name:		aview
Version:	1.3.0rc1
Release:	4
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/aa-project/%{name}-%{version}.tar.gz
# Source0-md5:	093f298e7787591e229b59d039c72f4d
URL:		http://aa-project.sourceforge.net/aview/
BuildRequires:	XFree86-libs
BuildRequires:	autoconf
BuildRequires:	aalib-devel
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aview is an high quality ascii-art image(pnm) browser and
animation(fli/flc) player useful especially with lynx browser.

Supports: stdio, curses, slang, X11, gpm, linux-console.

Features: Save into many formats (html, text, ansi, more/less etc...),
Contrast, Bright, Gamma control,Image zooming/unzooming, Three
dithering modes, Hidden "bonus" features :), Inversion, Support for
bright, dim, inverse attributes/extended character set

%description -l pl
aview jest wysokiej jako¶ci przegl±dark± obrazków (pnm) i animacji
(fli/flc) w formacie ASCII, u¿yteczn± zw³aszcza w po³±czeniu z
przegl±dark± lynx.

Wspiera: stdio, curses, slang, X11, gpm, linux-console.

Opcje: zapisywanie w wielu formatach (html, txt, ansi, more/less,
etc...), mo¿liwo¶æ ustawienia kontrastu, jasno¶ci i nasycenia, zoom,
trzy poziomy ditheringu, itp. oraz ukryte opcje "bonusowe" :)

%prep
%setup -q -n %{name}-1.3.0

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# groff link instead of full copy
echo ".so aview.1" > $RPM_BUILD_ROOT%{_mandir}/man1/asciiview.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE ChangeLog AUTHORS NEWS README README.flip TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
