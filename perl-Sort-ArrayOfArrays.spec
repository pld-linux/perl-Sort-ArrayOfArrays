#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Sort
%define		pnam	ArrayOfArrays
Summary:	Sort::ArrayOfArrays Perl module
Summary(pl.UTF-8):   Moduł Perla Sort::ArrayOfArrays
Name:		perl-Sort-ArrayOfArrays
Version:	1.00
Release:	3
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	31bb796e6ad39a66a145cecef75b01fd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort::ArrayOfArrays was written to sort an arbitrary array of arrays,
in powerful, different ways.

%description -l pl.UTF-8
Moduł Sort::ArrayOfArrays służy do sortowania tablic tablic na wiele
różnych sposobów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Sort/ArrayOfArrays.pm
%{_mandir}/man3/*
