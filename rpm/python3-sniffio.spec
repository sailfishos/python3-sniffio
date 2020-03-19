# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:       python3-sniffio
Summary:    Sniff out which async library your code is running under
Version:    1.1.0
Release:    1
License:    MIT or ASL 2.0
URL:        https://pypi.org/project/sniffio/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-setuptools

%description
You’re writing a library. You’ve decided to be ambitious, and support multiple async I/O packages, like Trio, and asyncio, and … You’ve written a bunch of clever code to handle all the differences. But… how do you know which piece of clever code to run?

This is a tiny package whose only purpose is to let you detect which async library your code is running under.

%prep
%setup -q -n %{name}-%{version}/sniffio

%build
python3 ./setup.py build

%install
rm -rf %{buildroot}
python3 ./setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/sniffio
%{python3_sitearch}/sniffio-*.egg-info
