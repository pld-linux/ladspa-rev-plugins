%define		_name REV-plugins
Summary:	Stereo reverb LADSPA plugin
Summary(pl.UTF-8):	Wtyczka LADSPA - stereofoniczny pogłos
Name:		ladspa-rev-plugins
Version:	0.3.1
Release:	1
License:	GPL v2+
Group:		Applications/Sound
#Source0Download: http://users.skynet.be/solaris/linuxaudio/getit.html
Source0:	http://users.skynet.be/solaris/linuxaudio/downloads/%{_name}-%{version}.tar.bz2
# Source0-md5:	bca920c2cbf5e33989e7cafab6fbaee4
Patch0:		%{name}-misc_fixes.patch
URL:		http://users.skynet.be/solaris/linuxaudio/
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
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CPPFLAGS="-I. -fPIC -D_REENTRANT -Wall %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_PLUGINS_DIR=%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/g2reverb.so
