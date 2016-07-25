%global pkg_name felix-framework
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%global project felix
%global bundle org.apache.felix.framework
%global groupId org.apache.felix

Name:           %{?scl_prefix}%{pkg_name}
Version:        4.2.1
Release:        5.6%{?dist}
Summary:        Apache Felix Framework

License:        ASL 2.0
URL:            http://felix.apache.org
Source0:        http://www.apache.org/dist/%{project}/%{bundle}-%{version}-source-release.tar.gz

BuildArch:      noarch

BuildRequires: %{?scl_prefix}javapackages-tools
BuildRequires: %{?scl_prefix}felix-osgi-compendium
BuildRequires: %{?scl_prefix}felix-osgi-core
BuildRequires: %{?scl_prefix}maven-local
BuildRequires: %{?scl_prefix}maven-surefire-provider-junit
BuildRequires: %{?scl_prefix}apache-rat-plugin
BuildRequires: %{?scl_prefix}felix-parent

%description
Apache Felix Framework Interfaces and Classes.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{bundle}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x

%mvn_file : %{project}/%{bundle}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.1-5.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.1-5.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.1-5.4
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.1-5.3
- Remove requires on java

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.1-5.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.1-5.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.2.1-5
- Mass rebuild 2013-12-27

* Thu Nov 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.1-4
- Fix artifact file names

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 4.2.1-3
- Migrate away from mvn-rpmbuild (Resolves: #997514)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.1-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 15 2013 Mat Booth <fedora@matbooth.co.uk> - 4.2.1-1
- Update to latest upstream version rhbz #951006.

* Thu Feb 21 2013 Mat Booth <fedora@matbooth.co.uk> - 4.2.0-1
- Update to latest upstream version rhbz #895404.
- No longer need to remove maven-compiler-plugin invocation.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 4.0.2-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Aug 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0.2-4
- Remove maven-compiler-plugin invocation, resolves: #842591
- Remove unneeded BR: maven-invoker-plugin

* Thu Aug 16 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0.2-3
- Install NOTICE files

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 05 2012 Tomas Radej <tradej@redhat.com> - 4.0.2-1
- Updated to latest version
- Guidelines fixes

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 12 2010 Mat Booth <fedora@matbooth.co.uk> - 2.0.5-4
- Fix pom filename (Resolves rhbz#655798)
- Fix various packaging things according to new guidelines

* Tue Jul 13 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.0.5-3
- BR: maven-invoker-plugin required for maven-javadoc-plugin
- Use new names of the maven plgins
- Add license file to independent subpackage javadoc

* Tue Jul 13 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.0.5-2
- Use maven instead of ant

* Tue Jun 22 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.0.5-1
- Release 2.0.5
