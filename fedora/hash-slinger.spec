Summary: Generate and verify various DNS records such as SSHFP, TLSA and OPENPGPKEY
Name: hash-slinger
Version: 3.0
Release: 1%{?dist}
License: GPLv2+
Url:  http://people.redhat.com/pwouters/%{name}/
Source:  http://people.redhat.com/pwouters/%{name}/%{name}-%{version}.tar.gz
# Only to regenerate the man page, which is shipped per default
# Buildrequires: xmlto
BuildRequires: python3-devel
Requires: python3 >= 3.4
Requires: python3-dns, python3-unbound
Requires: openssh-clients >= 4, python3-m2crypto, python3-gnupg >= 0.3.7
BuildArch: noarch
Obsoletes: sshfp < 2.0
Provides: sshfp  = %{version}

%description
This package contains various tools to generate special DNS records:

sshfp       Generate RFC-4255 SSHFP DNS records from known_hosts files
            or ssh-keyscan
tlsa        Generate RFC-6698  TLSA DNS records via TLS
openpgpkey  Generate draft-ietf-dane-openpgpkey DNS records from OpenPGP
            keyrings
ipseckey    Generate RFC-4025 IPSECKEY DNS records on Libreswan
	    IPsec servers

This package has incorporated the old 'sshfp' and 'swede' commands/packages

%prep
%setup -q 

%build
make all

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install

%files 
%doc BUGS CHANGES README COPYING
%{_bindir}/*
%doc %{_mandir}/man1/*

%changelog
* Wed Sep 21 2016 Paul Wouters <pwouters@redhat.com> - 2.7-3
- Remove Requires: for python-argparse which is now part of python core

* Sun Jan 03 2016 Paul Wouters <pwouters@redhat.com> - 2.7-1
- Updated to 2.7 (updates to latest IETF drafts and RFCs, STARTTLS support)

* Tue Jan 06 2015 Paul Wouters <pwouters@redhat.com> - 2.6-1
- Updated to 2.6. Adds ipseckey, bugfixes for sshfp and openpgpkey

* Sat Jan 18 2014 Paul Wouters <pwouters@redhat.com> - 2.5-1
- Update to 2.5 which has OPENPGPKEY (draft 02) support
- Added python-gnupg requires

* Mon Jan  6 2014 Paul Wouters <pwouters@redhat.com> - 2.4-1
- Updated to 2.4 which updates OPENPGPKEY support

* Tue Dec 31 2013 Paul Wouters <pwouters@redhat.com> - 2.3-1
- Updated to 2.3 which adds support for OPENPGPKEY

* Mon Jun 24 2013 Paul Wouters <pwouters@redhat.com> - 2.2-1
- Updated to 2.2 which fixes tsla usage 0 and --ipv4/--ipv6 options

* Sat Sep 15 2012 Paul Wouters <pwouters@redhat.com> - 2.1-1
- Updated COPYING to properly reflect GPLv2 "or later"

* Fri Aug 24 2012 Paul Wouters <pwouters@redhat.com> - 2.0-1
- Initial package

