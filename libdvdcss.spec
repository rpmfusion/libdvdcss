Summary:    A portable abstraction library for DVD decryption
Name:       libdvdcss
Version:    1.6.0
Release:    %{autorelease}
License:    GPLv2+
Source:     http://www.videolan.org/pub/videolan/libdvdcss/%{version}/libdvdcss-%{version}.tar.xz
URL:        http://www.videolan.org/libdvdcss/

BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: meson

%description
This is a portable abstraction library for DVD decryption which is used by
the VideoLAN project, a full MPEG2 client/server solution.  You will need
to install this package in order to have encrypted DVD playback with the
VideoLAN client and the Xine navigation plugin.

%package devel
Summary:     Header files and development libraries for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%autosetup -p1

%build
%meson -Ddefault_library=shared

%meson_build

%install
%meson_install

# remove generated doc from build
mv %{buildroot}/usr/share/doc/libdvdcss docdir

%files
%license COPYING
%doc AUTHORS README.md
%{_libdir}/%{name}.so.2*

%files devel
%doc docdir/*
%{_includedir}/dvdcss
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
%autochangelog