#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Dist-CheckConflicts
Version  : 0.11
Release  : 3
URL      : http://search.cpan.org/CPAN/authors/id/D/DO/DOY/Dist-CheckConflicts-0.11.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/D/DO/DOY/Dist-CheckConflicts-0.11.tar.gz
Summary  : 'declare version conflicts for your dist'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-Dist-CheckConflicts-doc
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution Dist-CheckConflicts,
version 0.11:
declare version conflicts for your dist

%package doc
Summary: doc components for the perl-Dist-CheckConflicts package.
Group: Documentation

%description doc
doc components for the perl-Dist-CheckConflicts package.


%prep
%setup -q -n Dist-CheckConflicts-0.11

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/Dist/CheckConflicts.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
