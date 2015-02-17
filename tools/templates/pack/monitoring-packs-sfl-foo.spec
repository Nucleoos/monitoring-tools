#
# Example spec file for cdplayer app...
#
%define raw_name    {{ name }}
%define name        monitoring-packs-sfl-%{raw_name}
%define version     {{ date_long }}
%define release     1

Name:       %{name}
Version:    %{version}
Release:    %{release}%{?dist}
License: GPL v3
Summary: {{ desc }}
Group: Networking/Other
Source: http://monitoring.savoirfairelinux.com/%{name}_%{version}.orig.tar.gz
URL: http://monitoring.savoirfairelinux.com/
Distribution: Savoir-faire Linux
Vendor: Savoir-faire Linux
Packager: {{ author_name }} <{{ author_email }}>
BuildRoot:  %{_tmppath}/%{name}-%{version}
BuildRequires: python-sphinx
#Requires: python, python-dlnetsnmp

%description 
{{ desc }}

%prep
%setup -q -n %{name}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m 755 %{buildroot}/%{_libdir}/monitoring/packs/%{raw_name}
%{__cp} -r pack/* %{buildroot}/%{_libdir}/monitoring/packs/%{raw_name}
%{__install} -p -m 755 package.json %{buildroot}/%{_libdir}/monitoring/packs/%{raw_name}
%{__install} -d -m 755 %{buildroot}/%{_docdir}/monitoring/packs/%{raw_name}
%{__cp} -r doc/* %{buildroot}/%{_docdir}/monitoring/packs/%{raw_name}
%{__rm} %{buildroot}/%{_docdir}/monitoring/packs/%{raw_name}/conf.py
%{__install} -d -m 755 %{buildroot}/%{_mandir}/man1/monitoring/packs/%{raw_name}
sphinx-build -b man -d doc/build/doctrees/source doc %{buildroot}/%{_mandir}/man1/%{raw_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%docdir
%{_docdir}/monitoring/packs/%{raw_name}
%{_mandir}/man1/monitoring/packs/%{raw_name}
%config
%{_libdir}/monitoring/packs/

%changelog
* {{ date_rpm }} {{ author_name }} <{{ author_email }}>
- Initial Release
