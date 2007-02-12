#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Parser
Summary:	XML::Parser Perl module
Summary(cs.UTF-8):   Modul XML::Parser pro Perl
Summary(da.UTF-8):   Perlmodul XML::Parser
Summary(de.UTF-8):   XML::Parser Perl Modul
Summary(es.UTF-8):   Módulo de Perl XML::Parser
Summary(fr.UTF-8):   Module Perl XML::Parser
Summary(it.UTF-8):   Modulo di Perl XML::Parser
Summary(ja.UTF-8):   XML::Parser Perl モジュール
Summary(ko.UTF-8):   XML::Parser 펄 모줄
Summary(nb.UTF-8):   Perlmodul XML::Parser
Summary(pl.UTF-8):   Moduł Perla XML::Parser
Summary(pt.UTF-8):   Módulo de Perl XML::Parser
Summary(pt_BR.UTF-8):   Módulo Perl XML::Parser
Summary(ru.UTF-8):   Модуль для Perl XML::Parser
Summary(sv.UTF-8):   XML::Parser Perlmodul
Summary(uk.UTF-8):   Модуль для Perl XML::Parser
Summary(zh_CN.UTF-8):   XML::Parser Perl 模块
Name:		perl-XML-Parser
Version:	2.34
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	84d9e0001fe01c14867256c3fe115899
Patch0:		%{name}-paths.patch
BuildRequires:	expat-devel
BuildRequires:	perl-URI
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libwww
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
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
%{perl_vendorarch}/auto/XML/Parser/Expat/Expat.bs
%attr(755,root,root) %{perl_vendorarch}/auto/XML/Parser/Expat/Expat.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
