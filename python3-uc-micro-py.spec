#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Python port of uc.micro: micro subset of Unicode data files for linkify-it-py projects
Summary(pl.UTF-8):	Pythonowy port uc.micro: mały podzbiór plików danych unicode dla projektów linkify-it-py
Name:		python3-uc-micro-py
Version:	1.0.1
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/uc-micro-py/
Source0:	https://files.pythonhosted.org/packages/source/u/uc-micro-py/uc-micro-py-%{version}.tar.gz
# Source0-md5:	564838ccb47918b91a0c86242c8d25b2
URL:		https://pypi.org/project/uc-micro-py/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-cov
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python port of uc.micro - micro subset of Unicode data files
for linkify-it-py projects.

%description -l pl.UTF-8
Ten pakiet to pythonowy port projektu uc.micro - mały podzbiór plików
danych Unicode dla projektów linkify-it-py.

%prep
%setup -q -n uc-micro-py-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/uc_micro
%{py3_sitescriptdir}/uc_micro_py-%{version}-py*.egg-info
