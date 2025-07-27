Summary:    A portable abstraction library for DVD decryption
Name:       libdvdcss
Version:    1.4.3
Release:    9%{?dist}
License:    GPLv2+
Source:     http://www.videolan.org/pub/videolan/libdvdcss/%{version}/libdvdcss-%{version}.tar.bz2
URL:        http://www.videolan.org/libdvdcss/

BuildRequires: doxygen
BuildRequires: gcc


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
%autosetup


%build
%configure --disable-static
%make_build


%install
%make_install

# remove generated doc from build
mv %{buildroot}/usr/share/doc/libdvdcss docdir

# Remove all libtool archives
find %{buildroot} -regex ".*\.la$" -delete


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/%{name}.so.2*

%files devel
%doc docdir/*
%{_includedir}/dvdcss
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun Jul 27 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 21 2021 Leigh Scott <leigh123linux@gmail.com> - 1.4.3-1
- Update to 1.4.3

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.4.2-4
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 Xavier Bachelot <xavier@bachelot.org> - 1.4.2-3
- Add BR: gcc.
- Modernize specfile.

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Xavier Bachelot <xavier@bachelot.org> - 1.4.2-1
- Update to 1.4.2.

* Thu Feb 01 2018 Xavier Bachelot <xavier@bachelot.org> - 1.4.1-1
- Update to 1.4.1.
- Clean up spec.

* Fri Dec 18 2015 Remi Collet <remi@remirepo.net> - 1.4.0-1
- Update to 1.4.0

* Sun Aug 17 2014 Remi Collet <remi@remirepo.net> - 1.3.0-1
- Update to 1.3.0

* Wed Feb 27 2013 Remi Collet <remi@remirepo.net> - 1.2.13-1
- Update to 1.2.13

* Mon Mar 12 2012 Remi Collet <remi@remirepo.net> - 1.2.12-1
- Update to 1.2.12

* Sat Feb 18 2012 Remi Collet <remi@remirepo.net> - 1.2.11-2
- If unsure, assume the drive is of RPC-I type

* Mon Nov 21 2011 Remi Collet <remi@remirepo.net> - 1.2.11-1
- Update to 1.2.11

* Sat Oct 16 2010 Remi Collet <remi@remirepo.net> - 1.2.10-1
- F-14 rebuild

* Sun Sep 28 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.2.10-4
- Update to 1.2.10.

* Tue Sep 12 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.2.9-3
- Update to 1.2.9.

* Sun Aug  3 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.8.

* Wed Jun 25 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.7.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Tue Mar 11 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.6.

* Mon Feb  3 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.5.

* Fri Nov 15 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.4.

* Mon Oct 21 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.3.

* Thu Sep 26 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 8.0.

* Mon Aug 12 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.2.

* Mon Jun  3 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.1.

* Fri May 24 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.0.

* Thu May  2 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Mon Apr  8 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.1.1.

* Sun Nov  4 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Changed to the Ogle patched version of the lib.

* Mon Oct 22 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.
- Decided to put libdvdcss in a separate package since both videolan and the
  xine DVD menu plugin use it.

