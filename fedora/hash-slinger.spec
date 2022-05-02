Summary: Generate and verify various DNS records such as SSHFP, TLSA and OPENPGPKEY
Name: hash-slinger
Version: 3.1
Release: 2%{?dist}
License: GPLv2+
Url:  https://github.com/letoams/%{name}/
Source:  %{url}archive/%{version}/%{name}-%{version}.tar.gz
# Only to regenerate the man page, which is shipped per default
# Buildrequires: xmlto
BuildRequires: python3-devel, make
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
tlsa        Generate RFC-6698 TLSA DNS records via TLS
openpgpkey  Generate RFC-7929 OPENPGP DNS records from OpenPGP
            keyrings
ipseckey    Generate RFC-4025 IPSECKEY DNS records on Libreswan
            IPsec servers

This package has incorporated the old 'sshfp' and 'swede' commands/packages

%prep
%autosetup

%build
%make_build all

%install
%make_install

%files 
%license COPYING
%doc BUGS CHANGES README
%{_bindir}/*
%doc %{_mandir}/man1/*

%changelog
* Sun Jan 09 2022 Frank Crawford <frank@crawford.emu.id.au> - 3.1-2
- Update spec file following review

* Sat Sep 25 2021 Frank Crawford <frank@crawford.emu.id.au> - 3.1-1
- Updated to 3.1
- Add BuildRequires make
- Clean up spec file for Fedora review

* Sun Nov 03 2019 Frank Crawford <frank@crawford.emu.id.au> - 3.0-1
- Update to Python3

* Sat Apr 13 2019 Paul Wouters <pwouters@redhat.com> - 2.8-1
- Remove Requires: for python-argparse which is now part of python core

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

