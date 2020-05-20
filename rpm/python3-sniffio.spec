Name:       python3-sniffio
Summary:    Sniff out which async library your code is running under
Version:    1.1.0
Release:    1
License:    MIT or ASL 2.0
URL:        https://pypi.org/project/sniffio/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
You’re writing a library. You’ve decided to be ambitious, and support multiple async I/O packages, like Trio, and asyncio, and … You’ve written a bunch of clever code to handle all the differences. But… how do you know which piece of clever code to run?

This is a tiny package whose only purpose is to let you detect which async library your code is running under.

%prep
%setup -q -n %{name}-%{version}/sniffio

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%defattr(-,root,root,-)
%{python3_sitelib}/sniffio
%{python3_sitelib}/sniffio-*.egg-info
%exclude %{python3_sitelib}/sniffio/_tests
