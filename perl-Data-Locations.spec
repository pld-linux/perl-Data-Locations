#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Locations
Summary:	Data::Locations - magic insertion points in your data
Summary(pl):	Data::Locations - magiczne punkty wstawiania w danych
Name:		perl-Data-Locations
Version:	5.3
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
# note: "5.2-fixed" doesn't work with perl 5.8.2, plain 5.2 does
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	386d0681db7601631a005e2ac5e2485e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Locations - magic insertion points in your data.

%description -l pl
Data::Locations - magiczne punkty wstawiania w danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt CREDITS.txt README.txt
%{perl_vendorarch}/Data/Locations.pm
%dir %{perl_vendorarch}/auto/Data/Locations
%{perl_vendorarch}/auto/Data/Locations/Locations.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Data/Locations/Locations.so
%{_mandir}/man3/*
