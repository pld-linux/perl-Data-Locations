%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Locations
Summary:	Data::Locations perl module
Summary(pl):	Modu³ perla Data::Locations
Name:		perl-Data-Locations
Version:	5.2
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7d592ad82b1acf48747ea00a19c646bf
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Locations - magic insertion points in your data.

%description -l pl
Modu³ perla Data::Locations.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *txt
%{perl_vendorarch}/Data/Locations.pm
%dir %{perl_vendorarch}/auto/Data/Locations
%{perl_vendorarch}/auto/Data/Locations/Locations.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Data/Locations/Locations.so
%{_mandir}/man3/*
