# Archlinux 安装

1. LVM建立，参考[LVM](./LVM.md)

2. 格式化逻辑卷，参考[磁盘操作](./磁盘操作.md)

3. 挂载分区

    ```bash
    # mount /dev/ArchServer/lvroot /mnt
    ```

4. 选择镜像

    编辑/etc/pacman.d/mirrorlist，选择首选mirror。
    这个mirror列表也将通过pacstrap被复制并保存到系统中

    使用阿里镜像

        Server = http://mirrors.yun-idc.com/archlinux/$repo/os/$arch
        Server = http://mirrors.aliyun.com/archlinux/$repo/os/$arch

5. 安装基本系统

    ```bash
    # pacstrap /mnt base base-devel
    ```

6. Fstab

    ```bash
    # genfstab -U /mnt >> /mnt/etc/fstab
    ```

7. Chroot

    ```bash
    # arch-chroot /mnt /bin/bash
    ```

8. 时区

    ```bash
    # ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
    ```
    
    设置时间标准为UTC，并调整时间漂移

    ```bash
    # hwclock --systohc --utc
    ```

9. Locale

    编辑/etc/locale.gen

    ```bash
    # locale-gen
    ```

10. 主机名

    ```bash
    # echo myhostname > /etc/hostname
    ```

11. Grub

    ```bash
    # pacman -S grub

    # grub-install --target=i386-pc /dev/ArchServer/lvroot

    # grub-mkconfig -o /boot/grub/grub.cfg
    ```
