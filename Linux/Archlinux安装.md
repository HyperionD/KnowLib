# Archlinux 安装

1. 更新系统时间

    ```bash
    # timedatectl set-ntp true
    ```

2. 分区，boot单独分区不使用LVM管理

    ```bash
    # fdisk /dev/sda
    
    分区后：
    /dev/sda1 ---- boot
    /dev/sda2 ----使用LVM管理
    ```

3. 建立LVM
    
    ```bash
    # pvcreate /dev/sda2

    # vgcreate Arch /dev/sda2

    # lvcreate -L 2G Arch -n lvswap
    # lvcreate -L 10G Arch -n lvroot
    ```

4. 格式化分区
    
    ```bash
    # mkfs.ext4 /dev/sda1

    # mkswap /dev/Arch/lvswap
    # swapon /dev/Arch/lvswap

    # mkfs.ext4 /dev/Arch/lvroot
    ```

5. 挂载分区

    ```bash
    # mount /dev/Arch/lvroot /mnt

    # mkdir /mnt/boot
    # mount /dev/sda1 /mnt/boot
    ```

6. 选择镜像

    编辑/etc/pacman.d/mirrorlist，选择首选mirror。
    这个mirror列表也将通过pacstrap被复制并保存到系统中

    使用阿里镜像

        Server = http://mirrors.aliyun.com/archlinux/$repo/os/$arch

7. 安装基本系统

    ```bash
    # pacstrap /mnt base base-devel
    ```

8. Fstab

    ```bash
    # genfstab -U /mnt >> /mnt/etc/fstab
    ```

9. Chroot

    ```bash
    # arch-chroot /mnt /bin/bash
    ```

10. Locale

    编辑/etc/locale.gen

    ```bash
    # locale-gen
    ```

11. 主机名

    ```bash
    # echo myhostname > /etc/hostname
    ```

12. 修改/etc/mkinitcpio.conf(LVM需要)

    在block与filesystem这两项中间加入lvm2

    ```
    /etc/mkinitcpio.conf
    --------------------------
    HOOKS="base udev ... block lvm2 filesystemc"
    ```

13. Grub

    ```bash
    # pacman -S grub

    # grub-install --target=i386-pc /dev/sda

    # grub-mkconfig -o /boot/grub/grub.cfg
    ```
