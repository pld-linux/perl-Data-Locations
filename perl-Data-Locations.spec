%include	/usr/lib/rpm/macros.perl
Summary:	Data-Locations perl module
Summary(pl):	Modu³ perla Data-Locations
Name:		perl-Data-Locations
Version:	5.2
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/Data-Locations-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data-Locations - magic insertion points in your data.

%description -l pl
Modu³ perla Data-Locations.

%prep
%setup -q -n Data-Locations-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Data/Locations/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Data/Locations
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES.txt,CREDITS.txt,README.txt}.gz

%{perl_sitearch}/Data/Locations.pm

%dir %{perl_sitearch}/auto/Data/Locations
%{perl_sitearch}/auto/Data/Locations/.packlist
%{perl_sitearch}/auto/Data/Locations/Locations.bs
%attr(755,root,root) %{perl_sitearch}/auto/Data/Locations/Locations.so

%{_mandir}/man3/*
