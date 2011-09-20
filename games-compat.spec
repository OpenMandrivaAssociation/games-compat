Name:		games-compat
Summary:	Provides compatibility with binary Linux games
Version:	0.5
Release:	1
URL:		http://mandriva.com/
Group:		Games/Other
License:	GPL
ExclusiveArch: i586 x86_64

# -- Common requires/suggests --
# Basic common 32-bit libs
Requires: libopenssl1.0.0 libopenal1 libpng3 libstdc++6 
Requires: libstdc++5 libjpeg62 libfreetype2 libxpm4 libxmu6 libnas2 libgtk+2.0_0
# libpng packages was changed in 2012+ - so add deps on the new packages
# for that version
%if %mdkversion >= 201200
Requires: libpng15 libpng0
%endif
# 32bit SDL libs (first two are 'current arch', the rest are 32bit)
Requires: libSDL1.2_0 libSDL_mixer1.2_0 libSDL_ttf2.0_0 libSDL_net1.2_0
Requires: libSDL_image1.2_0
# These are nice to have, but are usually not hard deps
Suggests: libhal1
# Packages in 32bit contrib
%define contrib32Pkgs libstdc++2.10 libgtk+1.2 libopenssl0.9.8

%ifarch x86_64
# -- 64bit-only requires/suggests --
Requires: lib64SDL1.2_0 lib64SDL_mixer1.2_0 lib64SDL_ttf2.0_0
Requires: lib64SDL_net1.2_0 lib64SDL_image1.2_0 lib64gtk+2.0_0
# Packages in 32bit contrib can't be required, as contrib is not added by
# default on 64bit
Suggests: %contrib32Pkgs
# GTK engines, when using a 32bit app on 64bit they will look better if the
# engine is installed (but they're not strictly required)
Suggests: libgtk-engines2 libmurrine
%else
# -- 32bit-only requires/suggests --
Requires: %contrib32Pkgs
%endif

%ifarch x86_64
# This is a fugly hack to get a 32bit libdir on 64bit
%define libdir /usr/lib
%else
%define libdir %{_libdir}
%endif

%description
This package provides and depends upon libraries that is used in
many commercial Linux games. If you plan to run commercial Linux games
you should install this package. It may also help you run som non-free
software.

%install
mkdir -p %{buildroot}%{libdir}
ln -s libcrypto.so.1.0.0 %{buildroot}%{libdir}/libcrypto.so.2
ln -s libssl.so.1.0.0 %{buildroot}%{libdir}/libssl.so.2
ln -s libSDL-1.2.so.0 %{buildroot}%{libdir}/libSDL-1.1.so.0
ln -s libpng.so %{buildroot}%{libdir}/libpng.so.2
export DONT_SYMLINK_LIBS=1

%files 
%{libdir}/*
