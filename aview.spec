Summary:	ASCII-Art image browser and animation player
Summary(pl):	Przegl±darka obrazków i animacji w formacie ASCII
Name:		aview
Version:	1.2
Release:	4
License:	GPL
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Source0:	ftp://ftp.ta.jcu.cz/pub/aa/%{name}-%{version}.tar.gz
BuildRequires:	aalib-devel
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	XFree86-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aview is an high quality ascii-art image(pnm) browser and
animation(fli/flc) player usefull especially with lynx browser.

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
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir}

gzip -9nf README ANNOUNCE README.flip ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ANNOUNCE,README.flip,ChangeLog,TODO}.gz
%attr(755,root,root) %{_bindir}/*
