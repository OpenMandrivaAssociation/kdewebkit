%define major 5
%define libname %mklibname KF5WebKit %{major}
%define devname %mklibname KF5WebKit -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kdewebkit
Version:	5.83.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/portingAids/%{name}-%{version}.tar.xz
Summary: KDE Integration for QtWebKit
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Qt5WebKitWidgets)
BuildRequires: cmake(Qt5Designer)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Wallet)

%description
KDE Integration for QtWebKit.

%package -n %{libname}
Summary: KDE Integration for QtWebKit
Group: System/Libraries

%description -n %{libname}
KDE Integration for QtWebKit.

%package -n %{devname}
Summary: Development files for KDE Frameworks 5 QtWebKit integration
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for KDE Frameworks 5 QtWebKit integration.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}
%{_libdir}/qt5/plugins/designer/kdewebkit5widgets.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/modules/*
