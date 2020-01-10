Name:           gnome-font-viewer
Version:        3.8.0
%global         release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Release:        3%{?dist}
Summary:        Utility for previewing fonts for GNOME

Group:          Applications/System
License:        GPLv2+
#No URL for the package specifically, as of now
URL:            http://www.gnome.org/gnome-3/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gnome-font-viewer/%{release_version}/%{name}-%{version}.tar.xz

BuildRequires:  gnome-desktop3-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils

%description
Use gnome-font-viewer, the Font Viewer, to preview fonts and display
information about a specified font. You can use the Font Viewer to display the
name, style, type, size, version and copyright of the font.

%prep
%setup -q

%build
%configure --disable-silent-rules
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name} --with-gnome

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%files -f %{name}.lang
%doc COPYING NEWS

%{_bindir}/%{name}
%{_bindir}/gnome-thumbnail-font
%{_datadir}/applications/%{name}.desktop
%{_datadir}/thumbnailers/%{name}.thumbnailer


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.8.0-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.0-2
- Mass rebuild 2013-12-27

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Thu Mar  7 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Wed Feb 20 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-2
- Rebuilt for libgnome-desktop soname bump

* Thu Feb 07 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-1
- Update to 3.7.5

* Wed Jan 16 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.4-1
- Update to 3.7.4

* Fri Dec 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.3-1
- Update to 3.7.3

* Thu Dec  6 2012 Rui Matos <rmatos@redhat.com> - 3.6.2-1
- Update to 3.6.2

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Wed Jul 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Thu Jun 28 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Fri Jun  8 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.2-1
- Update to 3.5.2

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.1-1
- Update to 3.5.1

* Wed Mar 28 2012 Rui Matos <rmatos@redhat.com> - 3.4.0-3
- Use %%global instead of %%define
- Don't define Version as the result of macro expansions so that we
  don't break automated tools

* Wed Mar 28 2012 Rui Matos <rmatos@redhat.com> - 3.4.0-2
- Use rpm macros to define the version number
- Do verbose builds

* Tue Mar 27 2012 Rui Matos <rmatos@redhat.com> - 3.4.0-1
- Update to 3.4.0

* Mon Mar  5 2012 Rui Matos <rmatos@redhat.com> - 3.3.2.1-3
- spec file cleanup
- removed unneeded GConf2-devel BR
- call update-desktop-database to rebuild the MIME types cache

* Tue Dec 06 2011 Anuj More <anujmorex@gmail.com> - 3.3.2.1-2
- made some formating changes in the spec file

* Fri Nov 18 2011 Anuj More <anujmorex@gmail.com> - 3.3.2.1-1
- rebuilt

