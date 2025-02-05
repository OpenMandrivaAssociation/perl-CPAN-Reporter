%define upstream_name    CPAN-Reporter
%define upstream_version 1.2011

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32::Job\\)'
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Adds CPAN Testers reporting to CPAN.pm
License:	Apache License
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Config::Tiny)
BuildRequires:	perl(CPAN)
BuildRequires:	perl(Devel::Autoflush)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy::Recursive)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(File::pushd)
BuildRequires:	perl(IO::CaptureOutput)
BuildRequires:	perl(Parse::CPAN::Meta)
BuildRequires:	perl(Probe::Perl)
BuildRequires:	perl(Tee)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Reporter)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
The CPAN Testers project captures and analyses detailed results from
building and testing CPAN distributions on multiple operating systems and
multiple versions of Perl. This provides valuable feedback to module
authors and potential users to identify bugs or platform compatibility
issues and improves the overall quality and value of CPAN.

One way individuals can contribute is to send a report for each module that
they test or install. CPAN::Reporter is an add-on for the CPAN.pm module to
send the results of building and testing modules to the CPAN Testers
project. Full support for CPAN::Reporter is available in CPAN.pm as of
version 1.92.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README Changes LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*



