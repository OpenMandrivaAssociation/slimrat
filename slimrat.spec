%define beta beta2

Summary:	Utility for downloading files from Rapidshare, Depositfiles etc
Name:		slimrat
Version:	1.1
Release:	0.%{beta}.1
License:	MIT License
Group:		Networking/WWW
URL:		http://code.google.com/p/slimrat/
Source0:	http://slimrat.googlecode.com/files/%{name}-%{version}-%{beta}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Requires:	wget
BuildArch:	noarch

%description
Command line and GUI utility for downloading files from Rapidshare
(Free), Depositfiles etc on Linux. Written in perl, uses wget and GTK GUI.

%prep
%setup -q -n %{name}-%{version}-%{beta}

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r src/* %{buildroot}%{_datadir}/%{name}

mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -s ../../%{_datadir}/%{name}/%{name} %{name}
ln -s ../../%{_datadir}/%{name}/%{name}-gui %{name}-gui
popd

mkdir -p %{buildroot}%{_sysconfdir}
install -m 0644 %{name}.conf %{buildroot}%{_sysconfdir}

mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-gui
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

