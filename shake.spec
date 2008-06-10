Summary:	File shaker
Summary(pl.UTF-8):	Mieszacz plików
Name:		shake
Version:	0.29
Release:	1
License:	GPL
Group:		Applications
Source0:	http://download.savannah.nongnu.org/releases/shake/%{name}-%{version}.tar.bz2
# Source0-md5:	6713f30353be2891f60e64a5c899bfde
URL:		http://vleu.net/shake/
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
%setup -q

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
