Summary:	Stereo reverb LADSPA plugin
Summary(pl.UTF-8):	Wtyczka LADSPA - stereofoniczny pogłos
Name:		ladspa-rev-plugins
Version:	0.8.1
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/REV-plugins-%{version}.tar.bz2
# Source0-md5:	6e3063d0b30d1038a6bcd987114d9c71
Patch0:		%{name}-misc_fixes.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/ladspa/index.html
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This LADSPA plugin contains a digital implementation of the stereo
reverb effect.

%description -l pl.UTF-8
Ta wtyczka LADSPA zawiera cyfrową implementację stereofonicznego
efektu pogłosu.

%prep
%setup -q -n REV-plugins-%{version}
%patch0 -p1

%build
CPPFLAGS="%{rpmcppflags}" \
CXXFLAGS="%{rpmcxxflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} -C source \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_PLUGINS_DIR=%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/zita-reverbs.so
