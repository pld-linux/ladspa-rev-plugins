%define		_name REV-plugins
Summary:	Stereo reverb LADSPA plugin
Summary(pl):	Wtyczka LADSPA - stereofoniczny pog³os
Name:		ladspa-rev-plugins
Version:	0.2.1
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://users.skynet.be/solaris/linuxaudio/downloads/%{_name}-%{version}.tar.bz2
# Source0-md5:	faf912441ebb992c1bcd4959e3bf80e2
Patch0:		%{name}-misc_fixes.patch
URL:		http://users.skynet.be/solaris/linuxaudio/
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This LADSPA plugin contains a digital implementation of the stereo
reverb effect.

%description -l pl
Ta wtyczka LADSPA zawiera cyfrow± implementacjê stereofonicznego
efektu pog³osu.

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
%attr(755,root,root) %{_libdir}/ladspa/*.so
