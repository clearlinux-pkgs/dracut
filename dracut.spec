#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dracut
Version  : 049
Release  : 30
URL      : https://github.com/dracutdevs/dracut/archive/049.tar.gz
Source0  : https://github.com/dracutdevs/dracut/archive/049.tar.gz
Summary  : Initramfs generator using udev
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.0+ LGPL-2.1+
Requires: dracut-bin = %{version}-%{release}
Requires: dracut-data = %{version}-%{release}
Requires: dracut-license = %{version}-%{release}
Requires: dracut-man = %{version}-%{release}
Requires: cpio-bin
Requires: findutils-bin
Requires: libc-bin
BuildRequires : asciidoc
BuildRequires : kmod-dev
BuildRequires : libxslt
Patch1: 0001-Crypt-Using-uname-m-instead-arch-command.patch

%description
dracut contains tools to create bootable initramfses for the Linux
kernel. Unlike previous implementations, dracut hard-codes as little
as possible into the initramfs. dracut contains various modules which
are driven by the event-based udev. Having root on MD, DM, LVM2, LUKS
is supported as well as NFS, iSCSI, NBD, FCoE with the dracut-network
package.

%package bin
Summary: bin components for the dracut package.
Group: Binaries
Requires: dracut-data = %{version}-%{release}
Requires: dracut-license = %{version}-%{release}

%description bin
bin components for the dracut package.


%package data
Summary: data components for the dracut package.
Group: Data

%description data
data components for the dracut package.


%package dev
Summary: dev components for the dracut package.
Group: Development
Requires: dracut-bin = %{version}-%{release}
Requires: dracut-data = %{version}-%{release}
Provides: dracut-devel = %{version}-%{release}
Requires: dracut = %{version}-%{release}

%description dev
dev components for the dracut package.


%package license
Summary: license components for the dracut package.
Group: Default

%description license
license components for the dracut package.


%package man
Summary: man components for the dracut package.
Group: Default

%description man
man components for the dracut package.


%prep
%setup -q -n dracut-049
cd %{_builddir}/dracut-049
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576003787
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --libdir=/usr/lib
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1576003787
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dracut
cp %{_builddir}/dracut-049/COPYING %{buildroot}/usr/share/package-licenses/dracut/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install
## install_append content
release=%{release}
release_no_build=${release%.*}
echo "DRACUT_VERSION=%{version}-$release_no_build" > %{buildroot}/usr/lib/dracut/dracut-version.sh
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/dracut/dracut-functions
/usr/lib/dracut/dracut-functions.sh
/usr/lib/dracut/dracut-init.sh
/usr/lib/dracut/dracut-initramfs-restore
/usr/lib/dracut/dracut-install
/usr/lib/dracut/dracut-logger.sh
/usr/lib/dracut/dracut-version.sh
/usr/lib/dracut/modules.d/00bash/module-setup.sh
/usr/lib/dracut/modules.d/00bootchart/module-setup.sh
/usr/lib/dracut/modules.d/00dash/module-setup.sh
/usr/lib/dracut/modules.d/00systemd/module-setup.sh
/usr/lib/dracut/modules.d/00warpclock/module-setup.sh
/usr/lib/dracut/modules.d/00warpclock/warpclock.sh
/usr/lib/dracut/modules.d/01fips/fips-boot.sh
/usr/lib/dracut/modules.d/01fips/fips-noboot.sh
/usr/lib/dracut/modules.d/01fips/fips.sh
/usr/lib/dracut/modules.d/01fips/module-setup.sh
/usr/lib/dracut/modules.d/01systemd-initrd/module-setup.sh
/usr/lib/dracut/modules.d/02caps/README
/usr/lib/dracut/modules.d/02caps/caps.sh
/usr/lib/dracut/modules.d/02caps/module-setup.sh
/usr/lib/dracut/modules.d/02systemd-networkd/module-setup.sh
/usr/lib/dracut/modules.d/03modsign/load-modsign-keys.sh
/usr/lib/dracut/modules.d/03modsign/module-setup.sh
/usr/lib/dracut/modules.d/03rescue/module-setup.sh
/usr/lib/dracut/modules.d/04watchdog/module-setup.sh
/usr/lib/dracut/modules.d/04watchdog/watchdog-stop.sh
/usr/lib/dracut/modules.d/04watchdog/watchdog.sh
/usr/lib/dracut/modules.d/05busybox/module-setup.sh
/usr/lib/dracut/modules.d/10i18n/10-console.rules
/usr/lib/dracut/modules.d/10i18n/README
/usr/lib/dracut/modules.d/10i18n/console_init.sh
/usr/lib/dracut/modules.d/10i18n/module-setup.sh
/usr/lib/dracut/modules.d/10i18n/parse-i18n.sh
/usr/lib/dracut/modules.d/30convertfs/convertfs.sh
/usr/lib/dracut/modules.d/30convertfs/do-convertfs.sh
/usr/lib/dracut/modules.d/30convertfs/module-setup.sh
/usr/lib/dracut/modules.d/35network-legacy/dhclient-script.sh
/usr/lib/dracut/modules.d/35network-legacy/dhclient.conf
/usr/lib/dracut/modules.d/35network-legacy/dhcp-root.sh
/usr/lib/dracut/modules.d/35network-legacy/ifup.sh
/usr/lib/dracut/modules.d/35network-legacy/kill-dhclient.sh
/usr/lib/dracut/modules.d/35network-legacy/module-setup.sh
/usr/lib/dracut/modules.d/35network-legacy/net-genrules.sh
/usr/lib/dracut/modules.d/35network-legacy/parse-bond.sh
/usr/lib/dracut/modules.d/35network-legacy/parse-bridge.sh
/usr/lib/dracut/modules.d/35network-legacy/parse-ibft.sh
/usr/lib/dracut/modules.d/35network-legacy/parse-ifname.sh
/usr/lib/dracut/modules.d/35network-legacy/parse-ip-opts.sh
/usr/lib/dracut/modules.d/35network-legacy/parse-team.sh
/usr/lib/dracut/modules.d/35network-legacy/parse-vlan.sh
/usr/lib/dracut/modules.d/35network-manager/module-setup.sh
/usr/lib/dracut/modules.d/35network-manager/nm-config.sh
/usr/lib/dracut/modules.d/35network-manager/nm-run.sh
/usr/lib/dracut/modules.d/40network/ifname-genrules.sh
/usr/lib/dracut/modules.d/40network/module-setup.sh
/usr/lib/dracut/modules.d/40network/net-lib.sh
/usr/lib/dracut/modules.d/40network/netroot.sh
/usr/lib/dracut/modules.d/45ifcfg/module-setup.sh
/usr/lib/dracut/modules.d/45ifcfg/write-ifcfg.sh
/usr/lib/dracut/modules.d/45url-lib/module-setup.sh
/usr/lib/dracut/modules.d/45url-lib/url-lib.sh
/usr/lib/dracut/modules.d/50drm/module-setup.sh
/usr/lib/dracut/modules.d/50gensplash/README
/usr/lib/dracut/modules.d/50gensplash/gensplash-emergency.sh
/usr/lib/dracut/modules.d/50gensplash/gensplash-newroot.sh
/usr/lib/dracut/modules.d/50gensplash/gensplash-pretrigger.sh
/usr/lib/dracut/modules.d/50gensplash/module-setup.sh
/usr/lib/dracut/modules.d/50plymouth/module-setup.sh
/usr/lib/dracut/modules.d/50plymouth/plymouth-emergency.sh
/usr/lib/dracut/modules.d/50plymouth/plymouth-newroot.sh
/usr/lib/dracut/modules.d/50plymouth/plymouth-populate-initrd.sh
/usr/lib/dracut/modules.d/50plymouth/plymouth-pretrigger.sh
/usr/lib/dracut/modules.d/80cms/cms-write-ifcfg.sh
/usr/lib/dracut/modules.d/80cms/cmsifup.sh
/usr/lib/dracut/modules.d/80cms/cmssetup.sh
/usr/lib/dracut/modules.d/80cms/module-setup.sh
/usr/lib/dracut/modules.d/80lvmmerge/README.md
/usr/lib/dracut/modules.d/80lvmmerge/lvmmerge.sh
/usr/lib/dracut/modules.d/80lvmmerge/module-setup.sh
/usr/lib/dracut/modules.d/81cio_ignore/module-setup.sh
/usr/lib/dracut/modules.d/81cio_ignore/parse-cio_accept.sh
/usr/lib/dracut/modules.d/90btrfs/80-btrfs.rules
/usr/lib/dracut/modules.d/90btrfs/btrfs_device_ready.sh
/usr/lib/dracut/modules.d/90btrfs/btrfs_finished.sh
/usr/lib/dracut/modules.d/90btrfs/btrfs_timeout.sh
/usr/lib/dracut/modules.d/90btrfs/module-setup.sh
/usr/lib/dracut/modules.d/90crypt/crypt-cleanup.sh
/usr/lib/dracut/modules.d/90crypt/crypt-lib.sh
/usr/lib/dracut/modules.d/90crypt/crypt-run-generator.sh
/usr/lib/dracut/modules.d/90crypt/cryptroot-ask.sh
/usr/lib/dracut/modules.d/90crypt/module-setup.sh
/usr/lib/dracut/modules.d/90crypt/parse-crypt.sh
/usr/lib/dracut/modules.d/90crypt/parse-keydev.sh
/usr/lib/dracut/modules.d/90crypt/probe-keydev.sh
/usr/lib/dracut/modules.d/90dm/11-dm.rules
/usr/lib/dracut/modules.d/90dm/59-persistent-storage-dm.rules
/usr/lib/dracut/modules.d/90dm/dm-pre-udev.sh
/usr/lib/dracut/modules.d/90dm/dm-shutdown.sh
/usr/lib/dracut/modules.d/90dm/module-setup.sh
/usr/lib/dracut/modules.d/90dmraid/61-dmraid-imsm.rules
/usr/lib/dracut/modules.d/90dmraid/dmraid.sh
/usr/lib/dracut/modules.d/90dmraid/module-setup.sh
/usr/lib/dracut/modules.d/90dmraid/parse-dm.sh
/usr/lib/dracut/modules.d/90dmsquash-live-ntfs/module-setup.sh
/usr/lib/dracut/modules.d/90dmsquash-live/apply-live-updates.sh
/usr/lib/dracut/modules.d/90dmsquash-live/checkisomd5@.service
/usr/lib/dracut/modules.d/90dmsquash-live/dmsquash-generator.sh
/usr/lib/dracut/modules.d/90dmsquash-live/dmsquash-live-genrules.sh
/usr/lib/dracut/modules.d/90dmsquash-live/dmsquash-live-root.sh
/usr/lib/dracut/modules.d/90dmsquash-live/dmsquash-liveiso-genrules.sh
/usr/lib/dracut/modules.d/90dmsquash-live/iso-scan.sh
/usr/lib/dracut/modules.d/90dmsquash-live/module-setup.sh
/usr/lib/dracut/modules.d/90dmsquash-live/parse-dmsquash-live.sh
/usr/lib/dracut/modules.d/90dmsquash-live/parse-iso-scan.sh
/usr/lib/dracut/modules.d/90kernel-modules-extra/module-setup.sh
/usr/lib/dracut/modules.d/90kernel-modules/insmodpost.sh
/usr/lib/dracut/modules.d/90kernel-modules/module-setup.sh
/usr/lib/dracut/modules.d/90kernel-modules/parse-kernel.sh
/usr/lib/dracut/modules.d/90kernel-network-modules/module-setup.sh
/usr/lib/dracut/modules.d/90livenet/fetch-liveupdate.sh
/usr/lib/dracut/modules.d/90livenet/livenet-generator.sh
/usr/lib/dracut/modules.d/90livenet/livenetroot.sh
/usr/lib/dracut/modules.d/90livenet/module-setup.sh
/usr/lib/dracut/modules.d/90livenet/parse-livenet.sh
/usr/lib/dracut/modules.d/90lvm/64-lvm.rules
/usr/lib/dracut/modules.d/90lvm/lvm_scan.sh
/usr/lib/dracut/modules.d/90lvm/module-setup.sh
/usr/lib/dracut/modules.d/90lvm/parse-lvm.sh
/usr/lib/dracut/modules.d/90mdraid/59-persistent-storage-md.rules
/usr/lib/dracut/modules.d/90mdraid/65-md-incremental-imsm.rules
/usr/lib/dracut/modules.d/90mdraid/md-noddf.sh
/usr/lib/dracut/modules.d/90mdraid/md-noimsm.sh
/usr/lib/dracut/modules.d/90mdraid/md-shutdown.sh
/usr/lib/dracut/modules.d/90mdraid/mdmon-pre-shutdown.sh
/usr/lib/dracut/modules.d/90mdraid/mdmon-pre-udev.sh
/usr/lib/dracut/modules.d/90mdraid/mdraid-cleanup.sh
/usr/lib/dracut/modules.d/90mdraid/mdraid-needshutdown.sh
/usr/lib/dracut/modules.d/90mdraid/mdraid-waitclean.sh
/usr/lib/dracut/modules.d/90mdraid/mdraid_start.sh
/usr/lib/dracut/modules.d/90mdraid/module-setup.sh
/usr/lib/dracut/modules.d/90mdraid/parse-md.sh
/usr/lib/dracut/modules.d/90multipath/module-setup.sh
/usr/lib/dracut/modules.d/90multipath/multipath-shutdown.sh
/usr/lib/dracut/modules.d/90multipath/multipathd-needshutdown.sh
/usr/lib/dracut/modules.d/90multipath/multipathd-stop.sh
/usr/lib/dracut/modules.d/90multipath/multipathd.service
/usr/lib/dracut/modules.d/90multipath/multipathd.sh
/usr/lib/dracut/modules.d/90qemu-net/module-setup.sh
/usr/lib/dracut/modules.d/90qemu/module-setup.sh
/usr/lib/dracut/modules.d/90stratis/module-setup.sh
/usr/lib/dracut/modules.d/90stratis/stratisd-init.service
/usr/lib/dracut/modules.d/90stratis/stratisd-start.sh
/usr/lib/dracut/modules.d/90stratis/stratisd-stop.sh
/usr/lib/dracut/modules.d/91crypt-gpg/README
/usr/lib/dracut/modules.d/91crypt-gpg/crypt-gpg-lib.sh
/usr/lib/dracut/modules.d/91crypt-gpg/module-setup.sh
/usr/lib/dracut/modules.d/91crypt-loop/crypt-loop-lib.sh
/usr/lib/dracut/modules.d/91crypt-loop/module-setup.sh
/usr/lib/dracut/modules.d/91zipl/install_zipl_cmdline.sh
/usr/lib/dracut/modules.d/91zipl/module-setup.sh
/usr/lib/dracut/modules.d/91zipl/parse-zipl.sh
/usr/lib/dracut/modules.d/95cifs/cifs-lib.sh
/usr/lib/dracut/modules.d/95cifs/cifsroot.sh
/usr/lib/dracut/modules.d/95cifs/module-setup.sh
/usr/lib/dracut/modules.d/95cifs/parse-cifsroot.sh
/usr/lib/dracut/modules.d/95dasd/module-setup.sh
/usr/lib/dracut/modules.d/95dasd/parse-dasd.sh
/usr/lib/dracut/modules.d/95dasd_mod/module-setup.sh
/usr/lib/dracut/modules.d/95dasd_mod/parse-dasd-mod.sh
/usr/lib/dracut/modules.d/95dasd_rules/module-setup.sh
/usr/lib/dracut/modules.d/95dasd_rules/parse-dasd.sh
/usr/lib/dracut/modules.d/95dcssblk/module-setup.sh
/usr/lib/dracut/modules.d/95dcssblk/parse-dcssblk.sh
/usr/lib/dracut/modules.d/95debug/module-setup.sh
/usr/lib/dracut/modules.d/95fcoe-uefi/module-setup.sh
/usr/lib/dracut/modules.d/95fcoe-uefi/parse-uefifcoe.sh
/usr/lib/dracut/modules.d/95fcoe/cleanup-fcoe.sh
/usr/lib/dracut/modules.d/95fcoe/fcoe-edd.sh
/usr/lib/dracut/modules.d/95fcoe/fcoe-genrules.sh
/usr/lib/dracut/modules.d/95fcoe/fcoe-up.sh
/usr/lib/dracut/modules.d/95fcoe/lldpad.sh
/usr/lib/dracut/modules.d/95fcoe/module-setup.sh
/usr/lib/dracut/modules.d/95fcoe/parse-fcoe.sh
/usr/lib/dracut/modules.d/95fcoe/stop-fcoe.sh
/usr/lib/dracut/modules.d/95fstab-sys/module-setup.sh
/usr/lib/dracut/modules.d/95fstab-sys/mount-sys.sh
/usr/lib/dracut/modules.d/95iscsi/cleanup-iscsi.sh
/usr/lib/dracut/modules.d/95iscsi/iscsiroot.sh
/usr/lib/dracut/modules.d/95iscsi/module-setup.sh
/usr/lib/dracut/modules.d/95iscsi/mount-lun.sh
/usr/lib/dracut/modules.d/95iscsi/parse-iscsiroot.sh
/usr/lib/dracut/modules.d/95lunmask/fc_transport_scan_lun.sh
/usr/lib/dracut/modules.d/95lunmask/module-setup.sh
/usr/lib/dracut/modules.d/95lunmask/parse-lunmask.sh
/usr/lib/dracut/modules.d/95lunmask/sas_transport_scan_lun.sh
/usr/lib/dracut/modules.d/95nbd/module-setup.sh
/usr/lib/dracut/modules.d/95nbd/nbd-generator.sh
/usr/lib/dracut/modules.d/95nbd/nbdroot.sh
/usr/lib/dracut/modules.d/95nbd/parse-nbdroot.sh
/usr/lib/dracut/modules.d/95nfs/module-setup.sh
/usr/lib/dracut/modules.d/95nfs/nfs-lib.sh
/usr/lib/dracut/modules.d/95nfs/nfs-start-rpc.sh
/usr/lib/dracut/modules.d/95nfs/nfsroot-cleanup.sh
/usr/lib/dracut/modules.d/95nfs/nfsroot.sh
/usr/lib/dracut/modules.d/95nfs/parse-nfsroot.sh
/usr/lib/dracut/modules.d/95qeth_rules/module-setup.sh
/usr/lib/dracut/modules.d/95resume/module-setup.sh
/usr/lib/dracut/modules.d/95resume/parse-resume.sh
/usr/lib/dracut/modules.d/95resume/resume.sh
/usr/lib/dracut/modules.d/95rootfs-block/block-genrules.sh
/usr/lib/dracut/modules.d/95rootfs-block/module-setup.sh
/usr/lib/dracut/modules.d/95rootfs-block/mount-root.sh
/usr/lib/dracut/modules.d/95rootfs-block/parse-block.sh
/usr/lib/dracut/modules.d/95rootfs-block/rootfallback.sh
/usr/lib/dracut/modules.d/95ssh-client/module-setup.sh
/usr/lib/dracut/modules.d/95terminfo/module-setup.sh
/usr/lib/dracut/modules.d/95udev-rules/59-persistent-storage.rules
/usr/lib/dracut/modules.d/95udev-rules/61-persistent-storage.rules
/usr/lib/dracut/modules.d/95udev-rules/load-modules.sh
/usr/lib/dracut/modules.d/95udev-rules/module-setup.sh
/usr/lib/dracut/modules.d/95virtfs/module-setup.sh
/usr/lib/dracut/modules.d/95virtfs/mount-virtfs.sh
/usr/lib/dracut/modules.d/95virtfs/parse-virtfs.sh
/usr/lib/dracut/modules.d/95zfcp/module-setup.sh
/usr/lib/dracut/modules.d/95zfcp/parse-zfcp.sh
/usr/lib/dracut/modules.d/95zfcp_rules/module-setup.sh
/usr/lib/dracut/modules.d/95zfcp_rules/parse-zfcp.sh
/usr/lib/dracut/modules.d/95znet/module-setup.sh
/usr/lib/dracut/modules.d/95znet/parse-ccw.sh
/usr/lib/dracut/modules.d/96securityfs/module-setup.sh
/usr/lib/dracut/modules.d/96securityfs/securityfs.sh
/usr/lib/dracut/modules.d/97biosdevname/module-setup.sh
/usr/lib/dracut/modules.d/97biosdevname/parse-biosdevname.sh
/usr/lib/dracut/modules.d/97masterkey/README
/usr/lib/dracut/modules.d/97masterkey/masterkey.sh
/usr/lib/dracut/modules.d/97masterkey/module-setup.sh
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-cmdline-ask.service
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-cmdline-ask.sh
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-cmdline.service
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-cmdline.service.8
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-cmdline.service.8.asc
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-cmdline.sh
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-emergency.service
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-emergency.sh
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-initqueue.service
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-initqueue.service.8
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-initqueue.service.8.asc
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-initqueue.sh
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-mount.service
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-mount.service.8
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-mount.service.8.asc
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-mount.sh
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-mount.service
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-mount.service.8
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-mount.service.8.asc
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-mount.sh
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-pivot.service
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-pivot.service.8
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-pivot.service.8.asc
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-pivot.sh
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-trigger.service
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-trigger.service.8
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-trigger.service.8.asc
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-trigger.sh
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-udev.service
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-udev.service.8
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-udev.service.8.asc
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-udev.sh
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-shutdown.service
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-shutdown.service.8
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-shutdown.service.8.asc
/usr/lib/dracut/modules.d/98dracut-systemd/dracut-tmpfiles.conf
/usr/lib/dracut/modules.d/98dracut-systemd/emergency.service
/usr/lib/dracut/modules.d/98dracut-systemd/module-setup.sh
/usr/lib/dracut/modules.d/98dracut-systemd/rootfs-generator.sh
/usr/lib/dracut/modules.d/98ecryptfs/README
/usr/lib/dracut/modules.d/98ecryptfs/ecryptfs-mount.sh
/usr/lib/dracut/modules.d/98ecryptfs/module-setup.sh
/usr/lib/dracut/modules.d/98integrity/README
/usr/lib/dracut/modules.d/98integrity/evm-enable.sh
/usr/lib/dracut/modules.d/98integrity/ima-keys-load.sh
/usr/lib/dracut/modules.d/98integrity/ima-policy-load.sh
/usr/lib/dracut/modules.d/98integrity/module-setup.sh
/usr/lib/dracut/modules.d/98pollcdrom/module-setup.sh
/usr/lib/dracut/modules.d/98pollcdrom/pollcdrom.sh
/usr/lib/dracut/modules.d/98selinux/module-setup.sh
/usr/lib/dracut/modules.d/98selinux/selinux-loadpolicy.sh
/usr/lib/dracut/modules.d/98syslog/README
/usr/lib/dracut/modules.d/98syslog/module-setup.sh
/usr/lib/dracut/modules.d/98syslog/parse-syslog-opts.sh
/usr/lib/dracut/modules.d/98syslog/rsyslog.conf
/usr/lib/dracut/modules.d/98syslog/rsyslogd-start.sh
/usr/lib/dracut/modules.d/98syslog/rsyslogd-stop.sh
/usr/lib/dracut/modules.d/98syslog/syslog-cleanup.sh
/usr/lib/dracut/modules.d/98usrmount/module-setup.sh
/usr/lib/dracut/modules.d/98usrmount/mount-usr.sh
/usr/lib/dracut/modules.d/99base/dracut-lib.sh
/usr/lib/dracut/modules.d/99base/init.sh
/usr/lib/dracut/modules.d/99base/initqueue.sh
/usr/lib/dracut/modules.d/99base/loginit.sh
/usr/lib/dracut/modules.d/99base/memtrace-ko.sh
/usr/lib/dracut/modules.d/99base/module-setup.sh
/usr/lib/dracut/modules.d/99base/parse-root-opts.sh
/usr/lib/dracut/modules.d/99base/rdsosreport.sh
/usr/lib/dracut/modules.d/99fs-lib/fs-lib.sh
/usr/lib/dracut/modules.d/99fs-lib/module-setup.sh
/usr/lib/dracut/modules.d/99img-lib/img-lib.sh
/usr/lib/dracut/modules.d/99img-lib/module-setup.sh
/usr/lib/dracut/modules.d/99shutdown/module-setup.sh
/usr/lib/dracut/modules.d/99shutdown/shutdown.sh
/usr/lib/dracut/modules.d/99squash/clear-squash.sh
/usr/lib/dracut/modules.d/99squash/init.sh
/usr/lib/dracut/modules.d/99squash/module-setup.sh
/usr/lib/dracut/modules.d/99squash/setup-squash.sh
/usr/lib/dracut/modules.d/99squash/shutdown.sh
/usr/lib/dracut/modules.d/99squash/squash-mnt-clear.service
/usr/lib/dracut/modules.d/99uefi-lib/module-setup.sh
/usr/lib/dracut/modules.d/99uefi-lib/uefi-lib.sh
/usr/lib/dracut/skipcpio
/usr/lib/kernel/install.d/50-dracut.install
/usr/lib/kernel/install.d/51-dracut-rescue.install

%files bin
%defattr(-,root,root,-)
/usr/bin/dracut
/usr/bin/dracut-catimages
/usr/bin/lsinitrd
/usr/bin/mkinitrd

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/dracut
/usr/share/bash-completion/completions/lsinitrd

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/dracut.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dracut/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lsinitrd.1
/usr/share/man/man5/dracut.conf.5
/usr/share/man/man7/dracut.bootup.7
/usr/share/man/man7/dracut.cmdline.7
/usr/share/man/man7/dracut.kernel.7
/usr/share/man/man7/dracut.modules.7
/usr/share/man/man8/dracut-catimages.8
/usr/share/man/man8/dracut-cmdline.service.8
/usr/share/man/man8/dracut-initqueue.service.8
/usr/share/man/man8/dracut-mount.service.8
/usr/share/man/man8/dracut-pre-mount.service.8
/usr/share/man/man8/dracut-pre-pivot.service.8
/usr/share/man/man8/dracut-pre-trigger.service.8
/usr/share/man/man8/dracut-pre-udev.service.8
/usr/share/man/man8/dracut-shutdown.service.8
/usr/share/man/man8/dracut.8
/usr/share/man/man8/mkinitrd-suse.8
/usr/share/man/man8/mkinitrd.8
