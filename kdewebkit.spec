%define major 5
%define libname %mklibname KF5WebKit %{major}
%define devname %mklibname KF5WebKit -d
%define debug_package %{nil}

Name: kdewebkit
Version: 5.3.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: KDE Integration for QtWebKit
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Wallet)
BuildRequires: ninja

%description
KDE Integration for QtWebKit

%package -n %{libname}
Summary: KDE Integration for QtWebKit
Group: System/Libraries

%description -n %{libname}
KDE Integration for QtWebKit

%package -n %{devname}
Summary: Development files for KDE Frameworks 5 QtWebKit integration
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for KDE Frameworks 5 QtWebKit integration

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_prefix}/mkspecs/*
