Name:			ethtool
Version:		3.18
Release:		1
Summary:		Settings tool for Ethernet NICs

License:		GPLv2
Group:			Applications/System
Source:     	ethtool-%{version}.tar.gz

BuildRequires:	automake, autoconf
Conflicts:      filesystem < 3

%description
This utility allows querying and changing settings such as speed,
port, auto-negotiation, PCI locations and checksum offload on many
network devices, especially of Ethernet devices.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL='install -p' install

%files
%doc AUTHORS ChangeLog* COPYING LICENSE NEWS README
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
