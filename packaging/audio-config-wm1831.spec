Name:       audio-config-wm1831
Summary:    Audio configuration files
Version:    0.0.29
Release:    0
Group:      System/Audio
License:    Apache-2.0
BuildArch:  noarch
Source0:    audio-config-wm1831-%{version}.tar.gz
Requires(post): coreutils

%description
audio configuration files for spreadtrum devices such as ucm files.

%package orbis
Summary: Audio configuration files for orbis-wm1831
Group: System/Audio
License: Apache-2.0

%description orbis
audio configuration files for ORBIS

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/alsa/ucm/ORBIS
mkdir -p %{buildroot}/usr/share/alsa/ucm/DUMMY
mkdir -p %{buildroot}%{_prefix}/lib/udev/rules.d/
mkdir -p %{buildroot}/opt/etc/dump.d/module.d

%if "%{sec_product_feature_audio_tuning_mode}" == "R720"
cp -arf ORBIS/ucm/* %{buildroot}/usr/share/alsa/ucm/ORBIS
%else if "%{sec_product_feature_audio_tuning_mode}" == "R732"
cp -arf ORBIS/ucm-classic/* %{buildroot}/usr/share/alsa/ucm/ORBIS
%else
cp -arf ORBIS/ucm/* %{buildroot}/usr/share/alsa/ucm/ORBIS
%endif

install -m 644 ORBIS/rules/*.rules %{buildroot}%{_prefix}/lib/udev/rules.d/

cp -arf DUMMY/ucm/* %{buildroot}/usr/share/alsa/ucm/DUMMY
cp -a util/largo_reg_dump.sh %{buildroot}/opt/etc/dump.d/module.d/

%pre orbis
UCM_PATH=/usr/share/alsa/ucm
rm -rf $UCM_PATH/*

%files orbis
%manifest audio-config-wm1831.manifest
%defattr(-,root,root,-)
/usr/share/alsa/ucm/ORBIS/*
/usr/share/alsa/ucm/DUMMY/*
%{_prefix}/lib/udev/rules.d/*.rules
/opt/etc/dump.d/module.d/largo_reg_dump.sh
