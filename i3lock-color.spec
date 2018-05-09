Name:		i3lock-color
# '-' before letter replaced with '.'
Version:	2.11.c
Release:	1%{?dist}
Summary:	Improved improved screen locker - "the ricing fork of i3lock"

License:	BSD
URL:		https://github.com/PandorasFox/i3lock-color
# Note: Source0 needs to be updated for every release
Source0:	https://github.com/PandorasFox/i3lock-color/archive/2.11-c.tar.gz

# Upstream uses same binary name for forked version
Conflicts:	i3lock

BuildRequires:	git
BuildRequires:	gcc
BuildRequires:	automake
BuildRequires:	make
BuildRequires:	cairo-devel
BuildRequires:	libev-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libxcb
BuildRequires:	libxkbcommon
BuildRequires:	libxkbcommon-x11-devel
BuildRequires:	pam-devel
BuildRequires:	pkg-config
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-image-devel

%description
i3lock is a simple screen locker like slock. After starting it, you will see a white screen (you can configure the color/an image). You can return to your screen by entering your password. This fork allows color configuration.

%prep
# Note: version needs to be updated here as well
%setup -q -n %{name}-2.11-c
git init
git config user.email "you@example.com"
git config user.name "Your Name"
git add .
git commit -m "Requires git tag for version/non-debug build"
git tag -f "v%{version}"

%build
autoreconf -i
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc CHANGELOG README*
%license LICENSE
%{_bindir}/i3lock
%{_sysconfdir}/pam.d/i3lock
%{_mandir}/man1/i3lock.1*

%changelog
* Tue May 08 2018 Ian Hattendorf <ian@ianhattendorf.com> - 2.11-c.1
- Initial RPM spec

