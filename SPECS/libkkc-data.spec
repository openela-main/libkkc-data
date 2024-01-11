%global debug_package %{nil}

Name:		libkkc-data
Version:	0.2.7
Release:	12%{?dist}
Epoch:		1
Summary:	Language model data for libkkc

License:	GPLv3+
URL:		https://bitbucket.org/libkkc
Source0:	https://bitbucket.org/libkkc/libkkc-data/downloads/%{name}-%{version}.tar.xz

# Upstream commit https://github.com/ueno/libkkc/commit/ba1c1bd3eb86d887fc3689c3142732658071b5f7
Patch0:         libkkc-data-HEAD.patch
# bug 1720044
Patch1:	%{name}-1720044-reiwa.patch

BuildRequires:	python3-devel
BuildRequires:	python3-marisa

%description
The %{name} package contains the language model data that libkkc uses
at run time.


%prep
%setup -q
%patch0 -p1 -b .HEAD
%patch1 -p1 -b .reiwa


%build
%configure --disable-static PYTHON=python3
make %{?_smp_mflags}


%install
%make_install INSTALL="install -p"


%files
%doc COPYING
%{_libdir}/libkkc


%changelog
* Mon Jun 17 2019 Takao Fujiwara <tfujiwar@redhat.com> - 1:0.2.7-12
- Resolves: #1720044 - Include Reiwa/The new Japanese era

* Tue Aug 14 2018 Parag Nemade <pnemade AT redhat DOT com> - 1:0.2.7-11
- Resolves:rh#1615534: libkkc-data FTBFS for missing BuildRequires
- moved this package to use python3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 20 2013 Daiki Ueno <dueno@redhat.com> - 1:0.2.7-2
- bump release to avoid NVR conflict

* Fri Sep 20 2013 Daiki Ueno <dueno@redhat.com> - 1:0.2.7-1
- add COPYING to %%doc
- disable debuginfo
- add Epoch to avoid conflict with the libkkc package

* Tue Sep 17 2013 Daiki Ueno <dueno@redhat.com> - 0.2.7-1
- initial packaging for Fedora, splitting from libkkc

