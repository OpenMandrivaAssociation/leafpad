Summary:	Notepad clone
Name:		leafpad
Version:	0.8.19
Release:	1
License:	GPLv2+
Group:		Editors
Url:		http://tarot.freeshell.org/leafpad/
Source0:	http://download.savannah.gnu.org/releases/leafpad/%{name}-%{version}.tar.gz
Patch0:		leafpad-0.8.16-fix-str-fmt.patch
Patch1:		leafpad-0.8.17-fix-desktop.patch

BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-2.0)

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
%autopatch -p1

%build
%configure
%make_build WARN_CFLAGS=""

%install
%make_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING README
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/leafpad.*
%{_mandir}/man1/leafpad.1.zst

