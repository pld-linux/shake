Summary:	File shaker
Summary(pl.UTF-8):	Mieszacz plików
Name:		shake
Version:	1.0
Release:	1
License:	GPL v3+
Group:		Applications/File
#Source0Download: https://github.com/unbrice/shake/tags
Source0:	https://github.com/unbrice/shake/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e5759e180b765a6ff13e77d775652e92
URL:		https://vleu.net/projects/shake/
BuildRequires:	attr-devel
BuildRequires:	cmake >= 2.4
BuildRequires:	help2man
BuildRequires:	rpmbuild(macros) >= 1.605
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
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/shake
%attr(755,root,root) %{_bindir}/unattr
%{_mandir}/man8/shake.8*
%{_mandir}/man8/unattr.8*
