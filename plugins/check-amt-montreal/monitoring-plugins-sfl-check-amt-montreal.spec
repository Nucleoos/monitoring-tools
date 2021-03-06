%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}


Name:           monitoring-plugins-sfl-check-amt-montreal
Version:        2015.2.19.14.44
Release:        1%{?dist}
Summary:        Checks the numbers of warnings reported by the AMT trains in the Montreal area.

License:        GPLv3
URL:            https://github.com/savoirfairelinux/monitoring-tools
Source0:        https://github.com/savoirfairelinux/monitoring-tools/monitoring-plugins-sfl-check-amt-montreal_%{version}.orig.tar.gz

Requires:       python-shinkenplugins
BuildRequires:  python-setuptools

BuildArch:      noarch

%description
Checks the numbers of warnings reported by the AMT trains in the Montreal area.
More information is available on Github:
https://github.com/savoirfairelinux/sfl-monitoring-tools

%prep
%setup -q -n monitoring-plugins-sfl-check-amt-montreal


%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-lib=%{python_sitelib}
%{__mkdir_p} %{buildroot}/%{_libdir}/monitoring/plugins/sfl
%{__install} -p -m0755 check_amt_montreal %{buildroot}/%{_libdir}/monitoring/plugins/sfl
%{__install} -d -m 755 %{buildroot}/%{_docdir}/monitoring/plugins/%{name}
%{__cp} -r doc/source/ %{buildroot}/%{_docdir}/monitoring/plugins/%{name}
%{__install} -d -m 755 %{buildroot}/%{_mandir}/man1/monitoring/plugins/%{name}
sphinx-build -b man -d doc/build/doctrees/source doc %{buildroot}/%{_mandir}/man1/monitoring/plugins/%{name}

#%check
#cd %{buildroot}/%{python_sitelib}/shinkenplugins/plugins/ && %{__python} -c "import amt_montreal"


%files
%defattr(-,root,root,-)
%{python_sitelib}/*.egg-info
%dir %{python_sitelib}/shinkenplugins
%{python_sitelib}/shinkenplugins/plugins/amt_montreal
%{_libdir}/monitoring/plugins/sfl/check_amt_montreal
%docdir
%{_docdir}/monitoring/plugins/%{name}
%{_mandir}/man1/monitoring/plugins/%{name}

%changelog
* Thu Feb 19 2015 Matthieu Caneill <matthieu.caneill@savoirfairelinux.com> - 2015.2.19.14.44
- Initial package