%define name	leafpad
%define version	0.8.14
%define title 	Leafpad

Summary:	Notepad clone
Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
License:	GPLv2+

Group:		Editors

URL:		http://tarot.freeshell.org/leafpad/
Source0:	http://download.savannah.gnu.org/releases/leafpad/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Source2:	%{name}-32.png
Source3:	%{name}-16.png

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	gtk2-devel

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

%build
%configure2_5x
%make WARN_CFLAGS=""

%install
rm -rf %buildroot
%makeinstall_std

%find_lang %name --with-gnome

# icon
mkdir -p %buildroot/{%_liconsdir,%_iconsdir,%_miconsdir}
#install -m 644 src/pixmaps/%name.png %buildroot/%_datadir/pixmaps/%name.png
install -m 644 %SOURCE1 %buildroot/%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot/%_liconsdir/%name.png
install -m 644 %SOURCE3 %buildroot/%_iconsdir/%name.png

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
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name.png
%{_datadir}/icons/hicolor/*/apps/leafpad.*
