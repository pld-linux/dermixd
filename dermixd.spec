Summary:	DerMixD is a TCP-controlled music playing daemon
Summary(hu.UTF-8):	DerMixD egy TCP-n keresztül irányítható zenelejátszó démon
Name:		dermixd
Version:	1.6.2
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	http://thomas.orgis.org/dermixd/%{name}-%{version}.tar.bz2
# Source0-md5:	5d9c8f5f7f827658d554e7d4013c8f6a
Patch0:		%{name}-1.6.2.patch
URL:		http://thomas.orgis.org/dermixd/
BuildRequires:	libsndfile-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DerMixD is a TCP-controlled music playing daemon for GNU/Linux and
hopefully (at least in the future) other UNIX/POSIX systems. It's
inspiration is mixplayd, which does quite the same, but partly less
and partly more. And a bit different for sure.

%description -l hu.UTF-8
DerMixD egy TCP-n keresztül irányítható zenelejátszó démon
GNU/Linux-ra és remélhetőleg (legalább a jövőben) más UNIX/POSIX
rendszerekre is. Az ihlet a mixplayd nevű program, amely kicsit
hasonló, de egy kicsit kevesebb, kicsit több. És különbözik is tőle.


%package frontend
Summary:	DerMixD frontends (perl-modules and command-line utils)
Summary(hu.UTF-8):	DerMixD frontendek (perl-modulok és parancssori eszközök)
Group:		Applications/Sound

%description frontend
Two PERL Modules for talking to DerMixD:
- DerMixD::Base for basic communication
- DerMixD::Control for basic control with a bit smartness (using Base)

Two command line PERL script utilizing the Control module:
- dermixd-control for direct control and executing scripts of dermixd
  commands
- simple_player player script reading (absolute) file names from stdin
  and playing them

%description frontend -l hu.UTF-8
Két PERL modul:
- DerMixD::Base az alapvető kommunikációra
- DerMixD::Control az alapvető irányításra (a Base-t használja)

Két parancssori PERL-szkript a Control modult felhasználva:
- dermixd-control közvetlen irányításra és dermixd-szkriptek
  futtatására
- simple_player egy lejátszó szkript, amely (abszolút) fájlneveket
  olvas az stdin-ről és lejátssza őket


%prep
%setup -q
%patch -P0 -p1

%build
%{__make} gnu-alsa SNDFILE=yes VORBISFILE=yes

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
## base
install dermixd $RPM_BUILD_ROOT%{_bindir}
## frontend
install frontend/{dermixd-control,shuffle,simple_player} $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/DerMixD
install frontend/Param.pm $RPM_BUILD_ROOT%{perl_vendorlib}
install frontend/DerMixD/* $RPM_BUILD_ROOT%{perl_vendorlib}/DerMixD


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL NOTES* README DECODERS AUTHORS BUGS CHANGES ChangeLog
%attr(755,root,root) %{_bindir}/dermixd


%files frontend
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dermixd-control
%attr(755,root,root) %{_bindir}/shuffle
%attr(755,root,root) %{_bindir}/simple_player
%doc frontend/README
%dir %{perl_vendorlib}/DerMixD
%{perl_vendorlib}/Param.pm
%{perl_vendorlib}/DerMixD/*
