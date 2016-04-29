Name:           dracut
Version:        043
Release:        16
License:        GPL-2.0+ LGPL-2.1+
Summary:        Initramfs generator
Url:            https://dracut.wiki.kernel.org/
Group:          base
Source0:        https://www.kernel.org/pub/linux/utils/boot/dracut/dracut-043.tar.xz
Requires:       libc-bin
Requires:       findutils-bin
Requires:       cpio-bin
Patch1:         0002-Fix-default-udev-systemd-dir-detection-in-usr-merge-.patch

%description
Initramfs generator.
%package -n dracut-network
Summary:        Initramfs generator
Requires:       %{name} = %{version}

%description -n dracut-network
Initramfs generator.

%package -n dracut-caps
Summary:        Initramfs generator
Requires:       %{name} = %{version}
Requires:       libcap-bin

%description -n dracut-caps
Initramfs generator.

%package -n dracut-tools
Summary:        Initramfs generator
Requires:       %{name} = %{version}

%description -n dracut-tools
Initramfs generator.

%prep
%setup -q
%patch1 -p1

%build
./configure --disable-documentation

make all

%install
make install DESTDIR=%{buildroot} \
     libdir=%{_prefix}/lib \
     bindir=%{_bindir} \
     systemdsystemunitdir=%{_prefix}/lib/systemd/system \
     sysconfdir=%{_sysconfdir} mandir=%{_mandir}

release=%{release}
release_no_build=${release%.*}
echo "DRACUT_VERSION=%{version}-$release_no_build" > %{buildroot}/%{_prefix}/lib/dracut/dracut-version.sh

rm -fr %{buildroot}/%{_prefix}/lib/dracut/modules.d/01fips
rm -fr %{buildroot}/%{_prefix}/lib/dracut/modules.d/02fips-aesni

# remove gentoo specific modules
rm -fr %{buildroot}/%{_prefix}/lib/dracut/modules.d/50gensplash

# with systemd IMA and selinux modules do not make sense
rm -fr %{buildroot}/%{_prefix}/lib/dracut/modules.d/96securityfs
rm -fr %{buildroot}/%{_prefix}/lib/dracut/modules.d/97masterkey
rm -fr %{buildroot}/%{_prefix}/lib/dracut/modules.d/98integrity
rm -fr %{buildroot}/%{_prefix}/lib/dracut/modules.d/98selinux

mkdir -p %{buildroot}/boot/dracut
mkdir -p %{buildroot}%{_localstatedir}/lib/dracut/overlay
mkdir -p %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/dracut.log
mkdir -p %{buildroot}%{_sharedstatedir}/initramfs

# Ensure dracut is executable
chmod +x %{buildroot}%{_bindir}/dracut
chmod +x %{buildroot}%{_prefix}/lib/dracut/dracut-install

# Drop empty file
rm -f %{buildroot}%{_sysconfdir}/dracut.conf

%files
%{_bindir}/dracut
# compat symlink
%{_bindir}/mkinitrd
%{_bindir}/lsinitrd
%dir %{_prefix}/lib/dracut
%dir %{_prefix}/lib/dracut/modules.d
%{_prefix}/lib/dracut/dracut-functions.sh
%{_prefix}/lib/dracut/dracut-functions
%{_prefix}/lib/dracut/dracut-version.sh
%{_prefix}/lib/dracut/dracut-logger.sh
%{_prefix}/lib/dracut/dracut-initramfs-restore
%{_prefix}/lib/dracut/dracut-install
%{_prefix}/lib/dracut/skipcpio
%{_prefix}/lib/dracut/modules.d/00dash
%{_prefix}/lib/dracut/modules.d/00bootchart
%{_prefix}/lib/dracut/modules.d/00systemd-bootchart/module-setup.sh
%{_prefix}/lib/dracut/modules.d/00systemd/module-setup.sh
%{_prefix}/lib/dracut/modules.d/01systemd-initrd/module-setup.sh
%{_prefix}/lib/dracut/modules.d/02systemd-networkd/module-setup.sh
%{_prefix}/lib/dracut/modules.d/03rescue/module-setup.sh
%{_prefix}/lib/dracut/modules.d/04watchdog
%{_prefix}/lib/dracut/modules.d/05busybox
%{_prefix}/lib/dracut/modules.d/10i18n
%{_prefix}/lib/dracut/modules.d/30convertfs
%{_prefix}/lib/dracut/modules.d/45url-lib
%{_prefix}/lib/dracut/modules.d/50plymouth
%{_prefix}/lib/dracut/modules.d/50drm/module-setup.sh
%{_prefix}/lib/dracut/modules.d/80cms
%{_prefix}/lib/dracut/modules.d/90btrfs
%{_prefix}/lib/dracut/modules.d/90crypt
%{_prefix}/lib/dracut/modules.d/90dm
%{_prefix}/lib/dracut/modules.d/90dmraid
%{_prefix}/lib/dracut/modules.d/90dmsquash-live
%{_prefix}/lib/dracut/modules.d/90kernel-modules
%{_prefix}/lib/dracut/modules.d/90lvm
%{_prefix}/lib/dracut/modules.d/90mdraid
%{_prefix}/lib/dracut/modules.d/90multipath
%{_prefix}/lib/dracut/modules.d/90qemu
%{_prefix}/lib/dracut/modules.d/91crypt-gpg
%{_prefix}/lib/dracut/modules.d/91crypt-loop
%{_prefix}/lib/dracut/modules.d/95debug
%{_prefix}/lib/dracut/modules.d/95resume
%{_prefix}/lib/dracut/modules.d/95rootfs-block
%{_prefix}/lib/dracut/modules.d/95dasd
%{_prefix}/lib/dracut/modules.d/95dasd_mod
%{_prefix}/lib/dracut/modules.d/95fstab-sys
%{_prefix}/lib/dracut/modules.d/95zfcp
%{_prefix}/lib/dracut/modules.d/95terminfo
%{_prefix}/lib/dracut/modules.d/95udev-rules
%{_prefix}/lib/dracut/modules.d/95virtfs
%{_prefix}/lib/dracut/modules.d/97biosdevname
%{_prefix}/lib/dracut/modules.d/98dracut-systemd
%{_prefix}/lib/dracut/modules.d/98ecryptfs
%{_prefix}/lib/dracut/modules.d/98pollcdrom
%{_prefix}/lib/dracut/modules.d/98syslog
%{_prefix}/lib/dracut/modules.d/98usrmount
%{_prefix}/lib/dracut/modules.d/99base
%{_prefix}/lib/dracut/modules.d/99fs-lib
%{_prefix}/lib/dracut/modules.d/99img-lib
%{_prefix}/lib/dracut/modules.d/99shutdown
%{_prefix}/lib/dracut/modules.d/00bash/module-setup.sh
%{_prefix}/lib/dracut/modules.d/03modsign/load-modsign-keys.sh
%{_prefix}/lib/dracut/modules.d/03modsign/module-setup.sh
%{_prefix}/lib/dracut/modules.d/95dasd_rules/module-setup.sh
%{_prefix}/lib/dracut/modules.d/95dasd_rules/parse-dasd.sh
%{_prefix}/lib/dracut/modules.d/95fcoe-uefi/module-setup.sh
%{_prefix}/lib/dracut/modules.d/95fcoe-uefi/parse-uefifcoe.sh
%{_prefix}/lib/dracut/modules.d/95zfcp_rules/module-setup.sh
%{_prefix}/lib/dracut/modules.d/95zfcp_rules/parse-zfcp.sh
%{_prefix}/lib/dracut/modules.d/99uefi-lib/module-setup.sh
%{_prefix}/lib/dracut/modules.d/99uefi-lib/uefi-lib.sh
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_localstatedir}/log/dracut.log
%dir %{_sharedstatedir}/initramfs
%{_prefix}/lib/systemd/system/dracut-shutdown.service
%{_prefix}/lib/systemd/system/sysinit.target.wants/dracut-shutdown.service
%{_prefix}/lib/systemd/system/dracut-cmdline.service
%{_prefix}/lib/systemd/system/dracut-initqueue.service
%{_prefix}/lib/systemd/system/dracut-mount.service
%{_prefix}/lib/systemd/system/dracut-pre-mount.service
%{_prefix}/lib/systemd/system/dracut-pre-pivot.service
%{_prefix}/lib/systemd/system/dracut-pre-trigger.service
%{_prefix}/lib/systemd/system/dracut-pre-udev.service
%{_prefix}/lib/systemd/system/initrd.target.wants/dracut-cmdline.service
%{_prefix}/lib/systemd/system/initrd.target.wants/dracut-initqueue.service
%{_prefix}/lib/systemd/system/initrd.target.wants/dracut-mount.service
%{_prefix}/lib/systemd/system/initrd.target.wants/dracut-pre-mount.service
%{_prefix}/lib/systemd/system/initrd.target.wants/dracut-pre-pivot.service
%{_prefix}/lib/systemd/system/initrd.target.wants/dracut-pre-trigger.service
%{_prefix}/lib/systemd/system/initrd.target.wants/dracut-pre-udev.service
%{_prefix}/lib/kernel/install.d/50-dracut.install
%{_prefix}/lib/kernel/install.d/51-dracut-rescue.install
%{_datadir}/bash-completion/completions/dracut
%{_datadir}/bash-completion/completions/lsinitrd
%{_datadir}/pkgconfig/dracut.pc

%files -n dracut-network
%defattr(0644,root,root,0755)
%{_prefix}/lib/dracut/modules.d/40network
%{_prefix}/lib/dracut/modules.d/95fcoe
%{_prefix}/lib/dracut/modules.d/95iscsi
%{_prefix}/lib/dracut/modules.d/90livenet
%{_prefix}/lib/dracut/modules.d/90qemu-net
%{_prefix}/lib/dracut/modules.d/95cifs
%{_prefix}/lib/dracut/modules.d/95nbd
%{_prefix}/lib/dracut/modules.d/95nfs
%{_prefix}/lib/dracut/modules.d/95ssh-client
%{_prefix}/lib/dracut/modules.d/45ifcfg
%{_prefix}/lib/dracut/modules.d/95znet
%{_prefix}/lib/dracut/modules.d/90kernel-network-modules/module-setup.sh

%files -n dracut-caps
%defattr(0644,root,root,0755)
%{_prefix}/lib/dracut/modules.d/02caps

%files -n dracut-tools
%defattr(0644,root,root,0755)
%{_bindir}/dracut-catimages
%dir /boot/dracut
%dir %{_localstatedir}/lib/dracut
%dir %{_localstatedir}/lib/dracut/overlay
