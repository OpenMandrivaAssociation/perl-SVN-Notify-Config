%define module	SVN-Notify-Config
%define name	perl-%{module}
%define version	0.09.07
%define up_version	0.0907
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Config-driven Subversion notification
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/SVN/%{module}-%{up_version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(SVN::Notify)
BuildRequires:	perl(YAML)
BuildRequires:  perl(Module::Build)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module is a YAML-based configuration wrapper on SVN::Notify.

%prep
%setup -q -n %{module}-%{up_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
export LC_ALL=C
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/SVN
%{_mandir}/*/*



