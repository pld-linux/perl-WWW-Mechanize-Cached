#
# Conditional build:
# tests require internet connectivity
%bcond_with	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	Mechanize-Cached
Summary:	WWW::Mechanize::Cached - cache response to be polite
Summary(pl):	WWW::Mechanize::Cached - buforowanie odpowiedzi, aby zachowywaæ siê grzecznie
Name:		perl-WWW-Mechanize-Cached
Version:	1.32
Release:	1
# same as perl 5+
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	722c77e04e06a964e9389c0da3aa6fc4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Cache-Cache >= 1.02
BuildRequires:	perl-WWW-Mechanize >= 1.00
BuildRequires:	perl-Storable >= 2.08
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Cached::Mechanize Perl module uses the Cache::Cache hierarchy to
implement a caching mechanism.  This lets one perform repeated
requests without hammering a server impolitely.

%description -l pl
Modu³ Perla WWW::Cached::Mechanize wykorzystuje z hierarchiê
Cache::Cache do implementacji mechanizmu buforowania. Pozwala on na
powtarzanie zapytañ bez niegrzecznego nekania serwera.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/WWW/Mechanize/Cached.pm
%{_mandir}/man3/*
