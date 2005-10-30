Summary:	X.org video driver for Sun GX and Turbo GX video cards
Summary(pl):	Sterownik obrazu X.org dla kart graficznych Sun GX i Turbo GX
Name:		xorg-driver-video-suncg6
Version:	1.0.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-suncg6-%{version}.tar.bz2
# Source0-md5:	b2e793ebed88f96dfaca8f94dc9ab746
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
ExclusiveArch:	sparc sparcv9 sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Sun GX and Turbo GX video cards.

%description -l pl
Sterownik obrazu X.org dla kart graficznych Sun GX i Turbo GX.

%prep
%setup -q -n xf86-video-suncg6-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/suncg6_drv.so
%{_mandir}/man4/suncg6.4x*
