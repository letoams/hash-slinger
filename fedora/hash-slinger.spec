Summary: Generate various DNS records such as RFC-4255 SSHFP and RFC-698 TLSA
Name: hash-slinger
Version: 2.1
Release: 1%{?dist}
License: GPLv2+
Url:  http://people.redhat.com/pwouters/%{name}/
Source:  http://people.redhat.com/pwouters/%{name}/%{name}-%{version}.tar.gz
Group: Applications/Internet
# Only to regenerate the man page, which is shipped per default
# Buildrequires: xmlto
Requires: python-dns, python-argparse, unbound-python, python-ipaddr
Requires: openssh-clients >= 4, m2crypto
BuildArch: noarch
Obsoletes: sshfp < 2.0
Provides: sshfp  = %{version}

%description
This package contains various tools to generate special DNS records:

sshfp   Generate RFC-4255 SSHFP DNS records from known_hosts files
        or ssh-keyscan
tlsa    Generate RFC-6698  TLSA DNS records via TLS

It pulls in software from 'sshfp' and 'swede'

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
* Sat Sep 15 2012 Paul Wouters <pwouters@redhat.com> - 2.1-1
- Updated COPYING to properly reflect GPLv2 "or later"

* Fri Aug 24 2012 Paul Wouters <pwouters@redhat.com> - 2.0-1
- Initial package

