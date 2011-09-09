Name:		games-compat
Summary:	Provides compatibility with binary Linux games
Version:	0.4
Release:	1
URL:		http://mandriva.com/
Group:		Games/Other
License:	GPL
# The requires are versioned to ensure we pull in the 32bit versions, and not 64bit
# versions
Requires:	libopenssl1.0.0 libopenal1 libSDL1.2_0 libpng3 libstdc++6 libstdc++5
# libstdc++2.10 is in 32bit contrib, so it can't be a requirement on 64bit
%ifarch x86_64
Suggests:   libstdc++2.10
%else
Requires:   libstdc++2.10
%endif

%ifarch x86_64
# This is a fugly hack to get a 32bit libdir on 64bit
%define libdir /usr/lib
%else
%define libdir %{_libdir}
%endif

%description
This package provides and depends upon libraries that is used in
many commercial Linux games. If you are having problems running some
commercial games, you should install this package.

%install
mkdir -p %{buildroot}%{libdir}
ln -s libcrypto.so.1.0.0 %{buildroot}%{libdir}/libcrypto.so.2
ln -s libssl.so.1.0.0 %{buildroot}%{libdir}/libssl.so.2
ln -s libSDL-1.2.so.0 %{buildroot}%{libdir}/libSDL-1.1.so.0
ln -s libpng.so %{buildroot}%{libdir}/libpng.so.2
export DONT_SYMLINK_LIBS=1

%files 
%{libdir}/*
