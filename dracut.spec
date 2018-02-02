Name:           dracut
Version:        046
Release:        22
License:        GPL-2.0+ LGPL-2.1+
Summary:        Initramfs generator
Url:            https://dracut.wiki.kernel.org/
Group:          base
Source0:        https://www.kernel.org/pub/linux/utils/boot/dracut/dracut-046.tar.xz
Requires:       libc-bin
Requires:       findutils-bin
Requires:       cpio-bin
BuildRequires:  kmod-dev
Patch0:          0001-Crypt-Using-uname-m-instead-arch-command.patch

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

%prep
%setup -q
%patch0 -p1

%build
./configure --disable-documentation

make all

%install
make install DESTDIR=%{buildroot} \
     libdir=/usr/lib \
     bindir=/usr/bin \
     systemdsystemunitdir=/usr/lib/systemd/system \
     sysconfdir=/etc mandir=/usr/share/man

release=%{release}
release_no_build=${release%.*}
echo "DRACUT_VERSION=%{version}-$release_no_build" > %{buildroot}/usr/lib/dracut/dracut-version.sh

rm -fr %{buildroot}/usr/lib/dracut/modules.d/01fips
rm -fr %{buildroot}/usr/lib/dracut/modules.d/02fips-aesni

# remove gentoo specific modules
rm -fr %{buildroot}/usr/lib/dracut/modules.d/50gensplash

# with systemd IMA and selinux modules do not make sense
rm -fr %{buildroot}/usr/lib/dracut/modules.d/96securityfs
rm -fr %{buildroot}/usr/lib/dracut/modules.d/97masterkey
rm -fr %{buildroot}/usr/lib/dracut/modules.d/98integrity
rm -fr %{buildroot}/usr/lib/dracut/modules.d/98selinux

# Ensure dracut is executable
chmod +x %{buildroot}%{_bindir}/dracut
chmod +x %{buildroot}/usr/lib/dracut/dracut-install

# Drop empty file
rm -f %{buildroot}%{_sysconfdir}/dracut.conf

%files
/usr/bin/dracut
/usr/bin/dracut-catimages
# compat symlink
/usr/bin/mkinitrd
/usr/bin/lsinitrd
%dir /usr/lib/dracut
%dir /usr/lib/dracut/modules.d
/usr/lib/dracut/dracut-init.sh
/usr/lib/dracut/dracut-functions.sh
/usr/lib/dracut/dracut-functions
/usr/lib/dracut/dracut-version.sh
/usr/lib/dracut/dracut-logger.sh
/usr/lib/dracut/dracut-initramfs-restore
/usr/lib/dracut/dracut-install
/usr/lib/dracut/skipcpio
/usr/lib/dracut/modules.d/00dash
/usr/lib/dracut/modules.d/00bootchart
/usr/lib/dracut/modules.d/00systemd-bootchart/module-setup.sh
/usr/lib/dracut/modules.d/00systemd/module-setup.sh
/usr/lib/dracut/modules.d/01systemd-initrd/module-setup.sh
/usr/lib/dracut/modules.d/02systemd-networkd/module-setup.sh
/usr/lib/dracut/modules.d/03rescue/module-setup.sh
/usr/lib/dracut/modules.d/04watchdog
/usr/lib/dracut/modules.d/05busybox
/usr/lib/dracut/modules.d/10i18n
/usr/lib/dracut/modules.d/30convertfs
/usr/lib/dracut/modules.d/45url-lib
/usr/lib/dracut/modules.d/50plymouth
/usr/lib/dracut/modules.d/50drm/module-setup.sh
/usr/lib/dracut/modules.d/80cms
/usr/lib/dracut/modules.d/80lvmmerge/README.md
/usr/lib/dracut/modules.d/80lvmmerge/lvmmerge.sh
/usr/lib/dracut/modules.d/80lvmmerge/module-setup.sh
/usr/lib/dracut/modules.d/90btrfs
/usr/lib/dracut/modules.d/90crypt
/usr/lib/dracut/modules.d/90dm
/usr/lib/dracut/modules.d/90dmraid
/usr/lib/dracut/modules.d/90dmsquash-live
/usr/lib/dracut/modules.d/90dmsquash-live-ntfs/module-setup.sh
/usr/lib/dracut/modules.d/90kernel-modules
/usr/lib/dracut/modules.d/90lvm
/usr/lib/dracut/modules.d/90mdraid
/usr/lib/dracut/modules.d/90multipath
/usr/lib/dracut/modules.d/90multipath-hostonly/module-setup.sh
/usr/lib/dracut/modules.d/90qemu
/usr/lib/dracut/modules.d/91crypt-gpg
/usr/lib/dracut/modules.d/91crypt-loop
/usr/lib/dracut/modules.d/95debug
/usr/lib/dracut/modules.d/95resume
/usr/lib/dracut/modules.d/95rootfs-block
/usr/lib/dracut/modules.d/95dasd
/usr/lib/dracut/modules.d/95dasd_mod
/usr/lib/dracut/modules.d/95fstab-sys
/usr/lib/dracut/modules.d/95zfcp
/usr/lib/dracut/modules.d/95terminfo
/usr/lib/dracut/modules.d/95udev-rules
/usr/lib/dracut/modules.d/95virtfs
/usr/lib/dracut/modules.d/97biosdevname
/usr/lib/dracut/modules.d/98dracut-systemd
/usr/lib/dracut/modules.d/98ecryptfs
/usr/lib/dracut/modules.d/98pollcdrom
/usr/lib/dracut/modules.d/98syslog
/usr/lib/dracut/modules.d/98usrmount
/usr/lib/dracut/modules.d/99base
/usr/lib/dracut/modules.d/99fs-lib
/usr/lib/dracut/modules.d/99img-lib
/usr/lib/dracut/modules.d/99shutdown
/usr/lib/dracut/modules.d/00bash/module-setup.sh
/usr/lib/dracut/modules.d/03modsign/load-modsign-keys.sh
/usr/lib/dracut/modules.d/03modsign/module-setup.sh
/usr/lib/dracut/modules.d/95dasd_rules/module-setup.sh
/usr/lib/dracut/modules.d/95dasd_rules/parse-dasd.sh
/usr/lib/dracut/modules.d/95fcoe-uefi/module-setup.sh
/usr/lib/dracut/modules.d/95fcoe-uefi/parse-uefifcoe.sh
/usr/lib/dracut/modules.d/95zfcp_rules/module-setup.sh
/usr/lib/dracut/modules.d/95zfcp_rules/parse-zfcp.sh
/usr/lib/dracut/modules.d/99uefi-lib/module-setup.sh
/usr/lib/dracut/modules.d/99uefi-lib/uefi-lib.sh
/usr/lib/systemd/system/dracut-shutdown.service
/usr/lib/systemd/system/sysinit.target.wants/dracut-shutdown.service
/usr/lib/systemd/system/dracut-cmdline.service
/usr/lib/systemd/system/dracut-initqueue.service
/usr/lib/systemd/system/dracut-mount.service
/usr/lib/systemd/system/dracut-pre-mount.service
/usr/lib/systemd/system/dracut-pre-pivot.service
/usr/lib/systemd/system/dracut-pre-trigger.service
/usr/lib/systemd/system/dracut-pre-udev.service
/usr/lib/systemd/system/initrd.target.wants/dracut-cmdline.service
/usr/lib/systemd/system/initrd.target.wants/dracut-initqueue.service
/usr/lib/systemd/system/initrd.target.wants/dracut-mount.service
/usr/lib/systemd/system/initrd.target.wants/dracut-pre-mount.service
/usr/lib/systemd/system/initrd.target.wants/dracut-pre-pivot.service
/usr/lib/systemd/system/initrd.target.wants/dracut-pre-trigger.service
/usr/lib/systemd/system/initrd.target.wants/dracut-pre-udev.service
/usr/lib/kernel/install.d/50-dracut.install
/usr/lib/kernel/install.d/51-dracut-rescue.install
/usr/share/bash-completion/completions/dracut
/usr/share/bash-completion/completions/lsinitrd
/usr/share/pkgconfig/dracut.pc

%files -n dracut-network
%defattr(0644,root,root,0755)
/usr/lib/dracut/modules.d/40network
/usr/lib/dracut/modules.d/95fcoe
/usr/lib/dracut/modules.d/95iscsi
/usr/lib/dracut/modules.d/90livenet
/usr/lib/dracut/modules.d/90qemu-net
/usr/lib/dracut/modules.d/95cifs
/usr/lib/dracut/modules.d/95nbd
/usr/lib/dracut/modules.d/95nfs
/usr/lib/dracut/modules.d/95ssh-client
/usr/lib/dracut/modules.d/45ifcfg
/usr/lib/dracut/modules.d/95znet
/usr/lib/dracut/modules.d/90kernel-network-modules/module-setup.sh

%files -n dracut-caps
%defattr(0644,root,root,0755)
/usr/lib/dracut/modules.d/02caps

