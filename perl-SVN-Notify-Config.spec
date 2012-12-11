%define upstream_name	SVN-Notify-Config
%define upstream_version	0.0911

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Config-driven Subversion notification
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SVN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(SVN::Notify)
BuildRequires:	perl(YAML)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Deep)
BuildRequires:  subversion
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module is a YAML-based configuration wrapper on SVN::Notify.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.91.100-1mdv2010.0
+ Revision: 404427
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.09.11-2mdv2009.0
+ Revision: 268720
- rebuild early 2009.0 package (before pixel changes)

* Fri Jun 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09.11-1mdv2009.0
+ Revision: 216488
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.09.07-2mdv2008.1
+ Revision: 138070
- fix tests

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Nov 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.09.07-1mdv2007.0
+ Revision: 86579
- new version

* Thu Nov 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.09.06-2mdv2007.1
+ Revision: 84675
- new release
- switch to Module::Build based build
- new version

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org> 0.08-1mdv2007.0
+ Revision: 54098
- 0.08
- disable test, are bad
- Import perl-SVN-Notify-Config

* Mon Jul 10 2006 Emmanuel Andry <eandry@mandriva.org> 0.07-1mdv2007.0
- 0.07

* Thu Dec 15 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-2mdk
- buildrequires perl-YAML

* Tue Nov 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdk
- first mdk release

