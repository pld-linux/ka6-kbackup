#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.08.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kbackup
Summary:	Kbackup
Name:		ka6-%{kaname}
Version:	24.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a5e521fd3815122de787895249501250
URL:		https://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-karchive-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-knotifications-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBackup is an application that lets you back up any folders or files
in a tar archive to a local folder, e.g. a locally mounted device like
a ZIP drive, USB stick, etc. or a remote URL.

Features

- Using profile files with definitions for Folders and files to be
  included or excluded from the backup
- The backup target can be either a locally mounted device like a ZIP
  drive, USB stick, etc. or any remote URL
- Running automated backups without using a graphical user interface

%description -l pl.UTF-8
KBackup jest aplikacją, która pozwala zapisać dowolne foldery lub
pliki w archiwum .tar do lokalnego katalogu, np. lokalnie
zamontowanego urządzenia jak dysk ZIP, pendrajw lub zdalny URL.

Właściwości

- Używa plików profili z definicjami folderów i plików, które mają
  włączone lub wyłączone z backupu
- Urządzenie docelowe, może być albo lokalnie zamontowanym dyskiem jak
  dysk ZIP, pendrajwem lub dowolnym zdalnym URLem
- Wykonuje automatyczne backupy bez używania graficznego interfejsu
  użytkownika

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbackup
%{_desktopdir}/org.kde.kbackup.desktop
%{_iconsdir}/hicolor/*x*/apps/kbackup.png
%{_iconsdir}/hicolor/16x16/mimetypes/text-x-kbp.png
%{_iconsdir}/hicolor/22x22/actions/kbackup_cancel.png
%{_iconsdir}/hicolor/22x22/actions/kbackup_runs.png
%{_iconsdir}/hicolor/22x22/actions/kbackup_start.png
%{_iconsdir}/hicolor/32x32/mimetypes/text-x-kbp.png
%{_datadir}/metainfo/org.kde.kbackup.appdata.xml
%{_datadir}/mime/packages/kbackup.xml
%lang(ca) %{_mandir}/ca/man1/kbackup.1*
%lang(it) %{_mandir}/it/man1/kbackup.1*
%{_mandir}/man1/kbackup.1*
%lang(nl) %{_mandir}/nl/man1/kbackup.1*
%lang(sv) %{_mandir}/sv/man1/kbackup.1*
%lang(tr) %{_mandir}/tr/man1/kbackup.1*
%lang(uk) %{_mandir}/uk/man1/kbackup.1*
%lang(de) %{_mandir}/de/man1/kbackup.1*
%lang(es) %{_mandir}/es/man1/kbackup.1*
%lang(sl) %{_mandir}/sl/man1/kbackup.1*
