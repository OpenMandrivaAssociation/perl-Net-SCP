%define upstream_name	 Net-SCP
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Net::SSH)
BuildRequires:	perl(String::ShellQuote)
BuildArch:	noarch

%description
Simple wrappers around ssh and scp commands.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%doc README
%{perl_vendorlib}/Net
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 404243
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.08-4mdv2009.0
+ Revision: 258104
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.08-3mdv2009.0
+ Revision: 246170
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2008.1
+ Revision: 104481
- update to new version 0.08

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-7mdv2008.0
+ Revision: 86709
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-6mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.07-5mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL
- use mkrel

* Mon Jun 06 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-4mdk 
- better url
- drop useless empty directories
- spec cleanup
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.07-3mdk
- fix buildrequires in a backward compatible way

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.07-2mdk 
- rebuild

* Wed Apr 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.07-1mdk
- new version
- rpmbuildupdate aware
- dir ownership
- no more explicit dependencies, let spec-helper do its job

