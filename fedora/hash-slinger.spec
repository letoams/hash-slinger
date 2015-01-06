Summary: Generate and verify various DNS records such as SSHFP, TLSA and OPENPGPKEY
Name: hash-slinger
Version: 2.6
Release: 1%{?dist}
License: GPLv2+
Url:  http://people.redhat.com/pwouters/%{name}/
Source:  http://people.redhat.com/pwouters/%{name}/%{name}-%{version}.tar.gz
Group: Applications/Internet
# Only to regenerate the man page, which is shipped per default
# Buildrequires: xmlto
Requires: python-dns, python-argparse, unbound-python, python-ipaddr, python-gnupg >= 0.3.5-2
Requires: openssh-clients >= 4, m2crypto
BuildArch: noarch
Obsoletes: sshfp < 2.0
Provides: sshfp  = %{version}

%description
This package contains various tools to generate special DNS records:

sshfp      Generate RFC-4255 SSHFP DNS records from known_hosts or ssh-keyscan
tlsa       Generate RFC-6698  TLSA DNS records via TLS
openpgpkey Generate RFC-<TBD> OPENPGPKEY DNS records
ipseckey   Generate RFC-4025 IPSECKEY DNS records on Libreswan IPsec servers

This package has incorporated the old 'sshfp' and 'swede' commands/packages

%prep
%setup -q 

%build
make all

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf ${RPM_BUILD_ROOT}

%files 
%doc BUGS CHANGES README COPYING
%{_bindir}/*
%doc %{_mandir}/man1/*

%changelog
* Mon Jan  6 2014 Paul Wouters <pwouters@redhat.com> - 2.4-1
- Updated to 2.4 which updates OPENPGPKEY support

* Tue Dec 31 2013 Paul Wouters <pwouters@redhat.com> - 2.3-1
- Updated to 2.3 which adds support for OPENPGPKEY

* Mon Jun 24 2013 Paul Wouters <pwouters@redhat.com> - 2.2-1
- New version

* Sat Sep 15 2012 Paul Wouters <pwouters@redhat.com> - 2.1-1
- Updated COPYING to properly reflect GPLv2 "or later"

* Fri Aug 24 2012 Paul Wouters <pwouters@redhat.com> - 2.0-1
- Initial package

