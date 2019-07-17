# see m4/${libname}.m4 />= for required version of particular library
%define		libcdata_ver	20190112
%define		libcerror_ver	20120425
%define		libcfile_ver	20160409
%define		libclocale_ver	20120425
%define		libcnotify_ver	20120425
%define		libcpath_ver	20180716
%define		libcsplit_ver	20120701
%define		libcthreads_ver	20160404
%define		libuna_ver	20181006
Summary:	Library to support (abstracted) basic file I/O
Summary(pl.UTF-8):	Biblioteka obsługująca (abstrakcyjne) podstawowe operacje we/wy dla plików
Name:		libbfio
Version:	20190112
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libbfio/releases
Source0:	https://github.com/libyal/libbfio/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	130fd3c263a85cf51a5e2eb06c601d3d
URL:		https://github.com/libyal/libbfio/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcpath-devel >= %{libcpath_ver}
BuildRequires:	libcsplit-devel >= %{libcsplit_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libcdata >= %{libcdata_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libcfile >= %{libcfile_ver}
Requires:	libclocale >= %{libclocale_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libcpath >= %{libcpath_ver}
Requires:	libcsplit >= %{libcsplit_ver}
Requires:	libcthreads >= %{libcthreads_ver}
Requires:	libuna >= %{libuna_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libbfio is a library to support (abstracted) basic file I/O.

%description -l pl.UTF-8
libbfio to biblioteka obsługująca (abstrakcyjne) podstawowe operacje
we/wy dla plików.

%package devel
Summary:	Header files for libbfio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libbfio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcdata-devel >= %{libcdata_ver}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libcfile-devel >= %{libcfile_ver}
Requires:	libclocale-devel >= %{libclocale_ver}
Requires:	libcnotify-devel >= %{libcnotify_ver}
Requires:	libcpath-devel >= %{libcpath_ver}
Requires:	libcsplit-devel >= %{libcsplit_ver}
Requires:	libcthreads-devel >= %{libcthreads_ver}
Requires:	libuna-devel >= %{libuna_ver}

%description devel
Header files for libbfio library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libbfio.

%package static
Summary:	Static libbfio library
Summary(pl.UTF-8):	Statyczna biblioteka libbfio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libbfio library.

%description static -l pl.UTF-8
Statyczna biblioteka libbfio.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libbfio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbfio.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbfio.so
%{_libdir}/libbfio.la
%{_includedir}/libbfio
%{_includedir}/libbfio.h
%{_pkgconfigdir}/libbfio.pc
%{_mandir}/man3/libbfio.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libbfio.a
