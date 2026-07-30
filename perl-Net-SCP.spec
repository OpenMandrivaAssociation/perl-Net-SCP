%define upstream_name	 Net-SCP
%define upstream_version 0.08.reprise
Name:		perl-%{upstream_name}
Version:	0.08.
Release:	1

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}/
Source0:	https://cpan.metacpan.org/authors/id/I/IV/IVAN/Net-SCP-0.08.reprise.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Net::SSH)
BuildRequires:	perl(String::ShellQuote)
BuildArch:	noarch

%description
Simple wrappers around ssh and scp commands.

%prep
%setup -q -n %{upstream_name}-%{version}

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


