Summary:	Library to support (abstracted) basic file I/O
Summary(pl.UTF-8):	Biblioteka obsługująca (abstrakcyjne) podstawowe operacje we/wy dla plików
Name:		libbfio
Version:	20150102
Release:	2
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libbfio/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2fc61eb9851303721eceae26bacde5c1
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libbfio/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcdata-devel >= 20150102
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcfile-devel >= 20140503
BuildRequires:	libclocale-devel >= 20120425
BuildRequires:	libcnotify-devel >= 20120425
BuildRequires:	libcpath-devel >= 20120701
BuildRequires:	libcsplit-devel >= 20120701
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libcthreads-devel >= 20130509
BuildRequires:	libuna-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libcdata >= 20150102
Requires:	libcerror >= 20120425
Requires:	libcfile >= 20140503
Requires:	libclocale >= 20120425
Requires:	libcnotify >= 20120425
Requires:	libcpath >= 20120701
Requires:	libcsplit >= 20120701
Requires:	libcstring >= 20120425
Requires:	libcthreads >= 20130509
Requires:	libuna >= 20120425
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
Requires:	libcdata-devel >= 20150102
Requires:	libcerror-devel >= 20120425
Requires:	libcfile-devel >= 20140503
Requires:	libclocale-devel >= 20120425
Requires:	libcnotify-devel >= 20120425
Requires:	libcpath-devel >= 20120701
Requires:	libcsplit-devel >= 20120701
Requires:	libcstring-devel >= 20120425
Requires:	libcthreads-devel >= 20130509
Requires:	libuna-devel >= 20120425

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
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
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
