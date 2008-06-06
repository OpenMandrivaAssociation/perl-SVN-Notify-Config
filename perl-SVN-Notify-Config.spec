%define module	SVN-Notify-Config
%define name	perl-%{module}
%define version	0.09.11
%define up_version	0.0911
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Config-driven Subversion notification
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/SVN/%{module}-%{up_version}.tar.gz
BuildRequires:	perl(SVN::Notify)
BuildRequires:	perl(YAML)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Deep)
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



