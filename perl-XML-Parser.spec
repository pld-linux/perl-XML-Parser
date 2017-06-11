#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Parser
Summary:	XML::Parser - A Perl module for parsing XML documents
Summary(cs.UTF-8):	XML::Parser - Modul do Perlu pro parsování XML dokumentů
Summary(da.UTF-8):	XML::Parser - Et perlmodul for fortolkning af XML-dokumenter
Summary(de.UTF-8):	XML::Parser - Ein Perl-Modul für das Parsen von XML-Dokumenten
Summary(es.UTF-8):	XML::Parser - Módulo Perl para pasear documentos XML
Summary(fr.UTF-8):	XML::Parser - Module Perl pour l'analyse de documents XML
Summary(it.UTF-8):	XML::Parser - Un modulo Perl per analizzare documenti XML
Summary(ja.UTF-8):	XMLドキュメント 解析用の perl モジュール です。
Summary(ko.UTF-8):	XML::Parser - XML 문서들을 파싱하는데 사용되는 펄 모줄
Summary(nb.UTF-8):	XML::Parser - En perlmodul for parsing av XML-dokumenter
Summary(pl.UTF-8):	XML::Parser - moduł Perla analizujący dokumenty XML
Summary(pt.UTF-8):	XML::Parser - Um módulo de Perl para analisar documentos em XML
Summary(sv.UTF-8):	XML::Parser - En perl-modul för att tolka XML-dokument
Summary(zh_CN.UTF-8):	用来解析 XML 文档 的 Perl 模块。
Name:		perl-XML-Parser
Version:	2.44
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af4813fe3952362451201ced6fbce379
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/XML-Parser/
BuildRequires:	expat-devel
BuildRequires:	perl-URI
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_tests:BuildRequires:	perl-libwww}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Parser - A Perl module for parsing XML documents.

%description -l cs.UTF-8
XML::Parser - Modul do Perlu pro parsování XML dokumentů.

%description -l da.UTF-8
XML::Parser - Et perlmodul for fortolkning af XML-dokumenter.

%description -l de.UTF-8
XML::Parser - Ein Perl-Modul für das Parsen von XML-Dokumenten.

%description -l es.UTF-8
XML::Parser - Módulo Perl para pasear documentos XML.

%description -l fr.UTF-8
XML::Parser - Module Perl pour l'analyse de documents XML.

%description -l it.UTF-8
XML::Parser - Un modulo Perl per analizzare documenti XML.

%description -l ja.UTF-8
XMLドキュメント 解析用の perl モジュール です。

%description -l ko.UTF-8
XML::Parser - XML 문서들을 파싱하는데 사용되는 펄 모줄.

%description -l nb.UTF-8
XML::Parser - En perlmodul for parsing av XML-dokumenter.

%description -l pl.UTF-8
XML::Parser - moduł Perla analizujący dokumenty XML.

%description -l pt.UTF-8
XML::Parser - Um módulo de Perl para analisar documentos em XML.

%description -l sv.UTF-8
XML::Parser - En perl-modul för att tolka XML-dokument.

%description -l zh_CN.UTF-8
用来解析 XML 文档 的 Perl 模块。

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	EXPATLIBPATH=%{_libdir} \
	EXPATINCPATH=%{_includedir}
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{perl_vendorlib}/XML/Parser/Style}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
rm -f samples/*~ samples/*.orig
install samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/*.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/XML/Parser.pm
%{perl_vendorarch}/XML/Parser
%dir %{perl_vendorarch}/auto/XML/Parser
%dir %{perl_vendorarch}/auto/XML/Parser/Expat
%attr(755,root,root) %{perl_vendorarch}/auto/XML/Parser/Expat/Expat.so
%dir %{perl_vendorlib}/XML/Parser/Style
%{_mandir}/man3/XML::Parser*.3pm*
%{_examplesdir}/%{name}-%{version}
