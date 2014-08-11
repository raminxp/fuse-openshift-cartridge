%global cartridgedir %{_libexecdir}/openshift/cartridges/fuse
%global frameworkdir %{_libexecdir}/openshift/cartridges/fuse

%global product_build_number 389

Name: openshift-origin-cartridge-fuse
Version: 6.1.0.redhat.%{product_build_number}
Release: 1%{?dist}
Summary: Fuse cartridge
Group: Development/Languages
License: ASL 2.0
URL: https://www.openshift.com
Source0: https://github.com/jboss-fuse/fuse-openshift-cartridge/archive/openshift-enterprise-rpm-6.1.zip
Source1: http://repository.jboss.org/nexus/content/groups/ea/org/jboss/fuse/jboss-fuse-full/6.1.0.redhat-%{product_build_number}/jboss-fuse-full-6.1.0.redhat-%{product_build_number}.zip
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Requires:      rubygem-openshift-origin-frontend-haproxy-sni-proxy

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Fuse cartridge for openshift.

%prep
%setup -q -n fuse-openshift-cartridge-openshift-enterprise-rpm-6.1

%build
unzip %SOURCE1
mv jboss-fuse-* usr

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{cartridgedir}
cp -r * %{buildroot}%{cartridgedir}/


%clean
rm -rf %{buildroot}


%post

%files
%defattr(-,root,root,-)
%dir %{cartridgedir}
%dir %{cartridgedir}/bin
%dir %{cartridgedir}/usr
%dir %{cartridgedir}/env
%dir %{cartridgedir}/metadata
%dir %{cartridgedir}/versions
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{frameworkdir}
%{cartridgedir}/metadata/manifest.yml
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE


%changelog
* Wed Jul 09 2014 Jon Anstey <janstey@gmail.com> 6.1.0.redhat.385-2
- https://bugzilla.redhat.com/show_bug.cgi?id=1109058
- https://bugzilla.redhat.com/show_bug.cgi?id=1109117

* Wed Jun 16 2014 Jon Anstey <janstey@gmail.com> 6.1.0.redhat.382-3
- Use 382 build no rather than 379
- Use redhat vendor name

* Wed Jun 11 2014 Jon Anstey <janstey@gmail.com> 6.1.0.redhat.382-1
- Fuse 6.1 rollup patch #1

* Wed Jun 11 2014 Jon Anstey <janstey@gmail.com> 6.1.0.redhat.379-1
- Fuse 6.1 GA cartridge