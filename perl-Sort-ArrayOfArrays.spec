%include	/usr/lib/rpm/macros.perl
%define		pdir	Sort
%define		pnam	ArrayOfArrays
Summary:	Sort::ArrayOfArrays Perl module
Summary(pl):	Modu³ Perla Sort::ArrayOfArrays
Name:		perl-Sort-ArrayOfArrays
Version:	1.00
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort::ArrayOfArrays was written to sort an arbitrary array of arrays,
in powerful, different ways.
	
%description -l pl
Modu³ Sort::ArrayOfArrays s³u¿y do sortowania tablic tablic na wiele
ró¿nych sposobów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Sort/ArrayOfArrays.pm
%{_mandir}/man3/*
