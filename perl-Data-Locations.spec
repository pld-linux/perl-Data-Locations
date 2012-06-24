%include	/usr/lib/rpm/macros.perl
Summary:	Data-Locations perl module
Summary(pl):	Modu� perla Data-Locations
Name:		perl-Data-Locations
Version:	5.2
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/Data-Locations-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data-Locations - magic insertion points in your data.

%description -l pl
Modu� perla Data-Locations.

%prep
%setup -q -n Data-Locations-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Data/Locations.pm
%dir %{perl_sitearch}/auto/Data/Locations
%{perl_sitearch}/auto/Data/Locations/Locations.bs
%attr(755,root,root) %{perl_sitearch}/auto/Data/Locations/Locations.so
%{_mandir}/man3/*
