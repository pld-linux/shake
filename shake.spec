Summary:	File shaker
Summary(pl.UTF-8):	Mieszacz plików
Name:		shake
Version:	0.999
Release:	1
License:	GPL
Group:		Applications
Source0:	http://download.savannah.nongnu.org/releases/shake/%{name}-%{version}.tar.bz2
# Source0-md5:	dd68f3619880ab0d92ed099dc2492120
URL:		http://vleu.net/shake/
BuildRequires:	attr-devel
BuildRequires:	cmake
BuildRequires:	help2man
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shake is a defragmenter that runs in userspace, without the need of
patching the kernel. There is no black magic involved: it works just
by rewriting fragmented files. But it has some heuristics that could
make it more efficient than other tools, including defrag and, maybe,
xfs_fsr.

%description -l pl.UTF-8
Shake jest defragmentatorem, który działa w przestrzeni użytkownika,
nie wymagając wprowadzania zmian do jądra. Nie ma tu żadnej czarnej
magii, działanie opiera się na przepisywaniu pofragmentowanych plików.
Użyte jest kilka heurystyk, które mogą sprawić, że program będzie
bardziej wydajny od innych narzędzi takich jak defrag, czy xfs_fsr.

%prep
%setup -q -n shake-fs-%{version}

%build
cd build
%{__cmake} ../
# fix paths
%{__sed} -i -e 's,/usr/local,/usr,g' CPackConfig.cmake
%{__sed} -i -e 's,/usr/local,/usr,g' CPackSourceConfig.cmake
%{__sed} -i -e 's,/usr/local,/usr,g' cmake_install.cmake

%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}
cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
