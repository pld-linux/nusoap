%include	/usr/lib/rpm/macros.php
Summary:	Web services based on SOAP 1.1, WSDL 1.1 and HTTP 1.0/1.1 for PHP
Summary(pl):	Us³ugi WWW oparte na SOAP 1.1, WSDL 1.1 i HTTP 1.0/1.1 dla PHP
Name:		nusoap
Version:	0.6.8
Release:	1
License:	GPL
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/nusoap/%{name}-%{version}.zip
# Source0-md5:	413ab57926fb093faa654efc10e60352
URL:		http://sourceforge.net/projects/nusoap/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
BuildRequires:	php-pear-Mail_Mime
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreq	'pear(class.*)'

%description
NuSOAP is a rewrite of SOAPx4, provided by NuSphere and Dietrich
Ayala. It is a set of PHP classes - no PHP extensions required - that
allow developers to create and consume web services based on SOAP 1.1,
WSDL 1.1 and HTTP 1.0/1.1.

%description -l pl
NuSOAP to przepisane od nowa SOAPx4 udostêpnione przez NuSphere i
Dietricha Ayalê. Jest to zbiór klas PHP - nie wymagaj±cych rozszerzeñ
PHP - umo¿liwiaj±cych programistom tworzenie i wykorzystywanie us³ug
WWW w oparciu o SOAP 1.1, WSDL 1.1 i HTTP 1.0/1.1.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/php/%{name}

install lib/*.php $RPM_BUILD_ROOT%{_datadir}/php/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lib/changelog samples
%{_datadir}/php/%{name}
