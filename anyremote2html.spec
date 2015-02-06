Name:		anyremote2html
Version:	1.4
Release:	2
Summary:	Web frontend for anyRemote Wireless remote control program
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://anyremote.sourceforge.net/
Source0:	http://sourceforge.net/projects/anyremote/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Requires:	python
Requires:	anyremote >= 5.4.1
BuildArch:	noarch

%description
Web frontend for anyRemote Wireless remote control program.
It acts as HTTP server and translates anyRemote commands to HTML.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%doc COPYING ChangeLog README
%{_bindir}/*
%{_datadir}/pixmaps/*



%changelog
* Thu Jan 19 2012 Andrey Bondrov <abondrov@mandriva.org> 1.4-1mdv2012.0
+ Revision: 762409
- imported package anyremote2html

