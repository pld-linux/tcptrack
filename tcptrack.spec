Summary:	tcptrack - console based application which displays information about TCP connections
Summary(pl.UTF-8):	tcptrack - konsolowa aplikacja pokazująca informacje o połączeniach TCP
Name:		tcptrack
Version:	1.3.0
Release:	2
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.rhythm.cx/~steve/devel/tcptrack/release/%{version}/source/%{name}-%{version}.tar.gz
# Source0-md5:	227baeb2f96758f7614f6f788b6a4d93
Patch0:		%{name}-gcc4.patch
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
list of connections in a manner similar to the Unix 'top' command. It
displays source and destination addresses and ports, connection state,
idle time, and bandwidth usage.

%description -l pl.UTF-8
tcptrack jest sniferem pokazującym informacje o połączeniach TCP,
które widzi na żądanym interfejsie. Wyświetla informacje na temat
stanu połączenia w formie listy podobnej do programu top. Pokazuje
adres źródłowy i docelowy, porty, stan połączenia, czas bezczynności i
zużycie pasma.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoheader}
#%{__autoconf}
#%{__automake}
CXXFLAGS="%{rpmcflags} -fexceptions -I/usr/include/ncurses"
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
