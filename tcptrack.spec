Summary:	tcptrack - console based application which displays information about TCP connections
Summary(pl):	tcptrack - konsolowa aplikacja pokazuj±ca informacje o po³±czeniach TCP
Name:		tcptrack
Version:	1.1.5
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.rhythm.cx/~steve/devel/tcptrack/release/%{version}/source/%{name}-%{version}.tar.gz
# Source0-md5:	ae360bede47cbfd75cae4eeaac90e8ed
URL:		http://www.rhythm.cx/~steve/devel/tcptrack/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tcptrack is a sniffer which displays information about TCP connections
it sees on a network interface. It passively watches for connections
on the network interface, keeps track of their state and displays a
list of connections in a manner similar to the unix 'top' command. It
displays source and destination addresses and ports, connection state,
idle time, and bandwidth usage.

%description -l pl
tcptrack jest sniferem pokazuj±cym informacje o po³±czeniach TCP,
które widzi na ¿±danym interfejsie. Wy¶wietla informacje na temat
stanu po³±czenia w formie listy podobnej do programu top. Pokazuje
adres ¼ród³owy i docelowy, porty, stan po³±czenia, czas bezczynno¶ci i
zu¿ycie pasma.

%prep
%setup -q

%build
%{__aclocal}
%{__autoheader}
#%{__autoconf}
#%{__automake}
CXXFLAGS="%{rpmcflags} -fexceptions -I%{_includedir}/ncurses"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
