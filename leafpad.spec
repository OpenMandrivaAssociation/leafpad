%define name	leafpad
%define version	0.8.9
%define section Applications/Editors
%define title 	Leafpad

Summary:	Notepad clone
Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
License:	GPL

Group:		Editors

URL:		http://tarot.freeshell.org/leafpad/
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.png
Source2:	%{name}-32.png
Source3:	%{name}-16.png

Patch0:		leafpad-0.7.0-gtk2.4-filechooser.patch.bz2
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

#%patch0 -p0 -b .filechooser

%build
%configure2_5x

%make WARN_CFLAGS=""

%install
rm -rf %buildroot
%makeinstall_std

%find_lang %name --with-gnome

# menu
mkdir -p %buildroot/%_menudir
cat > %buildroot/%_menudir/%name << EOF
?package(%name): \
command="%_bindir/%name" \
needs="x11" \
icon="%name.png" \
section="%section" \
title="%title" \
longtitle="%summary"
EOF

# icon
mkdir -p %buildroot/{%_liconsdir,%_iconsdir,%_miconsdir}
#install -m 644 src/pixmaps/%name.png %buildroot/%_datadir/pixmaps/%name.png
install -m 644 %SOURCE1 %buildroot/%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot/%_liconsdir/%name.png
install -m 644 %SOURCE3 %buildroot/%_iconsdir/%name.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/%{name}.desktop
%_menudir/%name
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name.png
