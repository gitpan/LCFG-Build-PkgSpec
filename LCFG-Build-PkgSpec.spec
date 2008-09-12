Name:           perl-LCFG-Build-PkgSpec
Version:        0.0.24
Release:        1
Summary:        Object-oriented interface to LCFG build metadata
License:        GPLv2
Group:          Development/Libraries
Source0:        LCFG-Build-PkgSpec-0.0.24.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:5.6.1
BuildRequires:  perl(Data::Structure::Util) >= 0.12
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose) >= 0.57
BuildRequires:  perl(MooseX::AttributeHelpers) >= 0.13
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(YAML::Syck) >= 0.98
BuildRequires:  perl(Date::Format) >= 1.16
Requires:       perl(Data::Structure::Util) >= 0.12
Requires:       perl(Moose) >= 0.57
Requires:       perl(MooseX::AttributeHelpers) >= 0.13
Requires:       perl(YAML::Syck) >= 0.98
Requires:       perl(Date::Format) >= 1.16
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This class provides an object-oriented interface to the LCFG build
tools metadata file. All simple fields are available through attribute
accessors. Specific methods are also provided for querying and
modifying the more complex data types (e.g. lists and hashes).

This class has methods for carrying out specific procedures related to
tagging releases with the LCFG build tools. It also has methods for
handling the old format LCFG build configuration files.

More information on the LCFG build tools is available from the website
http://www.lcfg.org/doc/buildtools/

%prep
%setup -q -n LCFG-Build-PkgSpec-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
/usr/bin/lcfg-cfg2meta
/usr/bin/lcfg-pkgcfg
%{perl_vendorlib}/LCFG/Build/PkgSpec.pm
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Fri Sep 12 2008 <<<< Release: 0.0.24 >>>>

* Fri Sep 12 2008 15:28 squinney
- Switched file path handling in lcfg-cfg2meta and lcfg-pkgcfg to
  using File::Spec

* Wed Sep 10 2008 14:59 squinney
- Small documentation tweaks to get links to other modules
  automatically generated

* Tue Sep 09 2008 15:30 squinney

* Tue Sep 09 2008 15:29 squinney
- Support fields in config.mk which use the ling-continuation
  backslash. Improved handling of attributes which can be either
  strings or array-refs so that they get properly transformed into
  array-refs. Removed the override of the new() method as it is no
  longer required. Made the LCFG::Build::PkgSpec class immutable to
  get a speed gain. Improved the README and other docs. Updated
  various Moose dependencies to ensure the code works correctly

* Wed Jul 23 2008 11:56 squinney

* Wed Jul 23 2008 11:56 squinney
- If not specified search the current working directory for the
  config.mk when using lcfg-cfg2meta

* Tue Jul 01 2008 15:37 squinney

* Tue Jul 01 2008 15:36 squinney
- Updated the tests which go with the config.mk parser

* Tue Jul 01 2008 15:32 squinney

* Tue Jul 01 2008 15:32 squinney
- When parsing a config.mk make the default license GPLv2 to be
  redhat compatible, also removed the specfile from the translate
  list and turned on the gencmake option

* Tue Jul 01 2008 11:37 squinney

* Tue Jul 01 2008 11:37 squinney
- Modified specfile to avoid installing *.in files

* Tue Jul 01 2008 09:53 squinney

* Tue Jul 01 2008 09:51 squinney
- Increased dependency on Moose to 0.51 to get consistent error
  messages

* Tue Jul 01 2008 09:51 squinney
- Moved to *.in files for perl libraries and executables

* Tue Jul 01 2008 09:51 squinney
- Moved to *.in files for perl libraries and executables

* Tue Jul 01 2008 09:34 squinney

* Thu Jun 05 2008 15:04 squinney

* Thu Jun 05 2008 15:03 squinney
- Added clone method to LCFG::Build::PkgSpec and accompanying tests

* Wed Jun 04 2008 16:35 squinney
- renamed perl-LCFG-Build-PkgSpec.spec to LCFG-Build-PkgSpec.spec

* Wed Jun 04 2008 15:01 squinney
- updated metadata files

* Wed Jun 04 2008 15:00 squinney

* Wed Jun 04 2008 15:00 squinney
- made build info attribute lazy

* Wed Jun 04 2008 14:47 squinney
- updated meta files

* Wed Jun 04 2008 14:47 squinney
- updated version string everywhere

* Wed Jun 04 2008 14:43 squinney

* Wed Jun 04 2008 14:37 squinney
- Added build info section support for lcfg metadata file

* Tue Jun 03 2008 13:40 squinney

* Tue Jun 03 2008 13:17 squinney
- Added dev_version and update_release methods

* Wed May 28 2008 12:29 squinney

* Wed May 28 2008 12:27 squinney
- [no log message]

* Wed May 28 2008 12:24 squinney
- Updated dependencies on Moose and MooseX::AttributeHelpers

* Wed May 28 2008 12:17 squinney
- updated specfile

* Wed May 28 2008 12:16 squinney

* Wed May 28 2008 12:15 squinney
- Renamed the smallest part of the version from 'level' to 'micro'.
  Added ability to query the individual parts of the version. Added
  an attribute to store the metafile name which can be used as a
  default when saving out the changed spec

* Wed May 07 2008 11:46 squinney
- version is now 0.0.10

* Wed May 07 2008 11:45 squinney

* Wed May 07 2008 11:45 squinney
- Added new tarname() method and associated tests and docs

* Wed Apr 30 2008 15:29 squinney
- Added fullname method

* Thu Mar 06 2008 09:45 squinney

* Thu Mar 06 2008 09:40 squinney
- Added support for dev versions

* Tue Mar 04 2008 10:06 squinney

* Tue Mar 04 2008 10:06 squinney
- Added support for setting a list of files to translate @FOO@
  macros

* Mon Mar 03 2008 12:09 squinney

* Mon Mar 03 2008 12:08 squinney
- new release number

* Mon Mar 03 2008 12:02 squinney
- Improved error message when creating a new pkgspec object and a
  required parameter is missing

* Mon Mar 03 2008 11:57 squinney
- Minimum version for Moose is now 0.38. This allows the setting of
  the release field as either undef or a validated string through
  the Maybe[] type syntax. Various tests were also updated as the
  error strings had changed slightly.

* Thu Feb 28 2008 12:09 squinney

* Thu Feb 28 2008 12:08 squinney
- Updated version

* Thu Feb 28 2008 12:08 squinney
- Added new --set, --skeleton options to lcfg-pkgcfg. Also added
  the ability to clone metadata files.

* Thu Feb 28 2008 12:08 squinney
- Added new --set, --skeleton options to lcfg-pkgcfg. Also added
  the ability to clone metadata files.

* Wed Feb 20 2008 14:03 squinney

* Wed Feb 20 2008 14:02 squinney
- Set version to 0.0.3

* Wed Feb 20 2008 14:02 squinney
- Added dependency on Date::Format

* Wed Feb 20 2008 14:02 squinney
- Added dependency on Date::Format

* Wed Feb 20 2008 13:52 squinney

* Wed Feb 20 2008 13:51 squinney
- Added version control information to lcfg.yml

* Wed Feb 20 2008 13:49 squinney
- updated tests to deal with the new date attribute handling

* Wed Feb 20 2008 13:47 squinney
- Improved date handling, it now defaults to 'DD/MM/YY HH:MM:SS'.
  Added update_date() method and made the update_major,
  update_minor and update_level methods use it

* Wed Feb 20 2008 13:45 squinney
- Added Changes file

* Tue Feb 19 2008 16:58 squinney
- Added lcfg.yml

* Tue Feb 19 2008 16:38 squinney
- First release of LCFG::Build::PkgSpec


