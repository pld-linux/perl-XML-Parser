%include	/usr/lib/rpm/macros.perl
Summary:	XML-Parser perl module
Summary(pl):	Modu³ perla XML-Parser
Name:		perl-XML-Parser
Version:	2.27
Release:	1
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-Parser-%{version}.tar.gz
Patch:		perl-XML-Parser-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-21
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
XML-Parser - module for parsing XML documents. 

%description -l pl
XML-Parser - modu³ analizuj±cy dokumenty XML.

%prep
%setup -q -n XML-Parser-%{version}
%patch -p0

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

rm -f samples/*~
install samples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/XML/Parser
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	$RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}/*.xml \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitearch}/XML/Parser.pm
%{perl_sitearch}/XML/Parser

%dir %{perl_sitearch}/auto/XML/Parser
%{perl_sitearch}/auto/XML/Parser/.packlist
%dir %{perl_sitearch}/auto/XML/Parser/Expat
%{perl_sitearch}/auto/XML/Parser/Expat/Expat.bs
%attr(755,root,root) %{perl_sitearch}/auto/XML/Parser/Expat/Expat.so

%{_mandir}/man3/*

/usr/src/examples/%{name}-%{version}
