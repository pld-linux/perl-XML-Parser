%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Parser
Summary:	XML::Parser Perl module
Summary(cs):	Modul XML::Parser pro Perl
Summary(da):	Perlmodul XML::Parser
Summary(de):	XML::Parser Perl Modul
Summary(es):	M�dulo de Perl XML::Parser
Summary(fr):	Module Perl XML::Parser
Summary(it):	Modulo di Perl XML::Parser
Summary(ja):	XML::Parser Perl �⥸�塼��
Summary(ko):	XML::Parser �� ����
Summary(no):	Perlmodul XML::Parser
Summary(pl):	Modu� Perla XML::Parser
Summary(pt):	M�dulo de Perl XML::Parser
Summary(pt_BR):	M�dulo Perl XML::Parser
Summary(ru):	������ ��� Perl XML::Parser
Summary(sv):	XML::Parser Perlmodul
Summary(uk):	������ ��� Perl XML::Parser
Summary(zh_CN):	XML::Parser Perl ģ��
Name:		perl-XML-Parser
Version:	2.34
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	84d9e0001fe01c14867256c3fe115899
Patch0:		%{name}-paths.patch
BuildRequires:	expat-devel
BuildRequires:	perl-URI
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Parser - A Perl module for parsing XML documents.

%description -l cs
XML::Parser - Modul do Perlu pro parsov�n� XML dokument�.

%description -l da
XML::Parser - Et perlmodul for fortolkning af XML-dokumenter.

%description -l de
XML::Parser - Ein Perl-Modul f�r das Parsen von XML-Dokumenten.

%description -l es
XML::Parser - M�dulo Perl para pasear documentos XML.

%description -l fr
XML::Parser - Module Perl pour l'analyse de documents XML.

%description -l it
XML::Parser - Un modulo Perl per analizzare documenti XML.

%description -l ja
XML�ɥ������ �����Ѥ� perl �⥸�塼�� �Ǥ���

%description -l ko
XML::Parser - XML �������� �Ľ��ϴµ� ���Ǵ� �� ����.

%description -l no
XML::Parser - En perlmodul for parsing av XML-dokumenter.

%description -l pl
XML::Parser - modu� Perla analizuj�cy dokumenty XML.

%description -l pt
XML::Parser - Um m�dulo de Perl para analisar documentos em XML.

%description -l sv
XML::Parser - En perl-modul f�r att tolka XML-dokument.

%description -l zh_CN
�������� XML �ĵ� �� Perl ģ�顣

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

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
