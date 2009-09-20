Summary:        Utility for downloading files from Rapidshare
Name:           slimrat
Version:        0.9.2
Release:        %mkrel 3
License:        MIT License
Group:          Networking/WWW
Source0:        http://slimrat.googlecode.com/files/%{name}-%{version}.tar.bz2
Patch0:         %{name}-youtube_plugin.patch
Patch1:         %{name}-wget.patch
URL:            http://code.google.com/p/slimrat/
Requires:       perl-base
Requires:       perl(Getopt::Long)
Requires:       gtk+2
Requires:       perl(Gtk2::GladeXML)
Requires:       perl(Gtk2::SimpleList)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Term::ANSIColor)
Requires:       perl(WWW::Mechanize)
Requires:       wget
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
Command line and GUI utility for downloading files from Rapidshare
(Free) on Linux. Written in perl, uses wget and GTK GUI.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/plugins
install slimrat $RPM_BUILD_ROOT%{_bindir}
sed -i -e 's,"+<\$quefile","+<"\,\ "\$quefile",' slimrat-gui
install slimrat-gui $RPM_BUILD_ROOT%{_bindir}
install Plugin.pm $RPM_BUILD_ROOT%{perl_vendorlib}
install slimrat.glade $RPM_BUILD_ROOT%{perl_vendorlib}
install plugins/*.pm $RPM_BUILD_ROOT%{perl_vendorlib}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/plugins
%{perl_vendorlib}/Plugin.pm
%{perl_vendorlib}/slimrat.glade
%{perl_vendorlib}/plugins/*.pm
