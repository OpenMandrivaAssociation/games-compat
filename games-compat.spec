%define	name	games-compat
%define	version 0.3
%define	release	%mkrel 6

Name:		%{name} 
Summary:	Provides compatibility with binary Linux games
Version:	%{version} 
Release:	%{release}
URL:		http://mandriva.com/
Group:		Games/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
Requires:	openssl-devel openal SDL-devel libpng libstdc++6 libstdc++5 libstdc++2.10

%description
This package provides and depends upon libraries that is used in
many commercial Linux games. If you are having problems running some
commercial games, you should install this package.

In addition to depending upon libraries used in many games
games-compat is known to fix:
- games bought from Garage Games
- games from ChronicLogic
- Raptor: Call of the shadows
- Bunnies
- ...and may fix other games

I also recommend that you install the loki_update package which
allows you to keep up to date with the latest patches for your
games.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
ln -s libcrypto.so $RPM_BUILD_ROOT%{_libdir}/libcrypto.so.2
ln -s libssl.so $RPM_BUILD_ROOT%{_libdir}/libssl.so.2
ln -s libSDL.so $RPM_BUILD_ROOT%{_libdir}/libSDL-1.1.so.0
ln -s libpng.so $RPM_BUILD_ROOT%{_libdir}/libpng.so.2
export DONT_SYMLINK_LIBS=1

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%{_libdir}/*
