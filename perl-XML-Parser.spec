%include	/usr/lib/rpm/macros.perl
Summary:	XML-Parser perl module
Summary(pl):	Modu� perla XML-Parser
Name:		perl-XML-Parser
Version:	2.29
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-Parser-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-21
BuildRequires:	perl >= 5.6
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML-Parser - module for parsing XML documents.

%description -l pl
XML-Parser - modu� analizuj�cy dokumenty XML.

%prep
%setup -q -n XML-Parser-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f samples/*~
install samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/*.xml \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/XML/Parser.pm
%{perl_sitearch}/XML/Parser
%dir %{perl_sitearch}/auto/XML/Parser
%dir %{perl_sitearch}/auto/XML/Parser/Expat
%{perl_sitearch}/auto/XML/Parser/Expat/Expat.bs
%attr(755,root,root) %{perl_sitearch}/auto/XML/Parser/Expat/Expat.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
