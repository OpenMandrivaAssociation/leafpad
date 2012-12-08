%define name	leafpad
%define version	0.8.18.1
%define	title	Leafpad

Summary:	Notepad clone
Name:		%{name}
Version:	%{version}
Release:	%mkrel 5
License:	GPLv2+

Group:		Editors

URL:		http://tarot.freeshell.org/leafpad/
Source0:	http://download.savannah.gnu.org/releases/leafpad/%{name}-%{version}.tar.gz
Patch0:		leafpad-0.8.16-fix-str-fmt.patch
Patch1:		leafpad-0.8.17-fix-desktop.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	gtk2-devel
BuildRequires:	intltool

%description
Leafpad is a simple GTK+ based text editor.
The user interface is similar to "notepad",
and it aims to be lighter than GEdit and
KWrite and to be as useful as them.

Following features are intended...

    * Minimum requirement
    * Minimal menu item
    * No toolbar
    * Single document interface (SDI)
    * Character coding auto detection

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_5x
%make WARN_CFLAGS=""

%install
rm -rf %buildroot
%makeinstall_std

%find_lang %name --with-gnome

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/leafpad.*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.18.1-2mdv2011.0
+ Revision: 666069
- mass rebuild

* Sun Jan 30 2011 Funda Wang <fwang@mandriva.org> 0.8.18.1-1
+ Revision: 634089
- BR intltool
- update to new version 0.8.18.1

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.17-4mdv2011.0
+ Revision: 606399
- rebuild

* Wed Mar 31 2010 Funda Wang <fwang@mandriva.org> 0.8.17-3mdv2010.1
+ Revision: 530155
- fix desktop file

  + Sandro Cazzaniga <kharec@mandriva.org>
    - fix rpmlint warning

* Sat Nov 07 2009 Funda Wang <fwang@mandriva.org> 0.8.17-1mdv2010.1
+ Revision: 462353
- New version 0.8.17

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.8.16-3mdv2010.0
+ Revision: 425506
- rebuild

* Tue Dec 23 2008 Funda Wang <fwang@mandriva.org> 0.8.16-2mdv2009.1
+ Revision: 317942
- fix str fmt
- drop old icons
- new version 0.8.16

* Wed Sep 03 2008 Frederik Himpe <fhimpe@mandriva.org> 0.8.15-1mdv2009.0
+ Revision: 279874
- update to new version 0.8.15

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.8.14-2mdv2009.0
+ Revision: 267801
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 0.8.14-1mdv2009.0
+ Revision: 200591
- New version 0.8.14

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Funda Wang <fwang@mandriva.org> 0.8.13-1mdv2008.1
+ Revision: 120500
- New version 0.8.13

  + Jérôme Soyer <saispo@mandriva.org>
    - New release 0.8.12

* Mon Apr 23 2007 Lenny Cartier <lenny@mandriva.org> 0.8.10-1mdv2008.0
+ Revision: 17341
- Update to 0.8.10
- Import leafpad



* Sat Apr 15 2006 Jerome Soyer <saispo@mandriva.org> 0.8.9-1mdk
- New release 0.8.9

* Sat Apr 07 2006 Jerome Soyer <saispo@mandriva.org> 0.8.8-1mdk
- New release 0.8.8

* Mon Feb 13 2006 Jerome Soyer <saispo@mandriva.org> 0.8.7-1mdk
- New release 0.8.7

* Fri Jan 20 2006 Jerome Soyer <saispo@mandriva.org> 0.8.6-1mdk
- 0.8.6

* Sun Nov 13 2005 Jerome Soyer <saispo@mandriva.org> 0.8.5-1mdk
- 0.8.5

* Mon Oct 03 2005 Lenny Cartier <lenny@mandriva.com> 0.8.4-1mdk
- 0.8.4

* Tue May 17 2005 Jerome Soyer <saispo@mandriva.org> 0.8.1-1mdk
- 0.8.1

* Mon May 09 2005 Jerome Soyer <saispo@mandriva.org> 0.8.0-1mdk
- New release

* Sun Dec 26 2004 Jerome Soyer <saispo@mandrake.org> 0.7.9-1mdk
- 0.7.9

* Sat Dec 04 2004 Jerome Soyer <saispo@mandrake.org> 0.7.8-1mdk
- 0.7.8
- Remove Patch0

* Fri Nov 19 2004 Jerome Soyer <saispo@mandrake.org> 0.7.7-1mdk
- 0.7.7

* Sun Nov 14 2004 Jerome Soyer <saispo@mandrake.org> 0.7.6-1mdk
- 0.7.6

* Tue Nov 09 2004 Jerome Soyer <saispo@mandrake.org> 0.7.5-1mdk
- 0.7.5

* Sat Oct 23 2004 Jerome Soyer <saispo@mandrake.org> 0.7.4-1mdk
- 0.7.4

* Mon Oct 18 2004 Jerome Soyer <saispo@mandrake.org> 0.7.3.1-1mdk
- 0.7.3.1

* Fri Oct 15 2004 Jerome Soyer <saispo@mandrake.org> 0.7.3-1mdk
- 0.7.3

* Sat Oct 02 2004 Jerome Soyer <saispo@mandrake.org> 0.7.2-1mdk
- 0.7.2

* Fri Sep 24 2004 Jerome Soyer <saispo@mandrake.org> 0.7.1-1mdk
- 0.7.1

* Sat Sep 17 2004 Jerome Soyer <saispo@mandrake.org> 0.7.0-1mdk
- new release
- Patch0 added GTK2.4 File chooser
- Added Menu & Icons
- Thks to UTUMI Hirosi <utuhiro78@yahoo.co.jp> for initial spec
