# LVM

LVM利用Linux内核的device-mapper来实现存储系统的虚拟化（系统分区独立于底层硬件）。 通过LVM，你可以实现存储空间的抽象化并在上面建立虚拟分区（virtual partitions），可以更简便地扩大和缩小分区，可以增删分区时无需担心某个硬盘上没有足够的连续空间

## LVM基本组成

1. **物理卷Physical volume(PV)**: 可以在上面建立卷组的媒介，可以是硬盘分区，也可以是硬盘本身或者回环文件（loopback file）

2. **卷组Volume group(VG)**: 将一组物理卷收集为一个管理单元。

3. **逻辑卷Logical volume(LV)**: 虚拟分区，由物理区域（physical extents）组成

4. **物理区域Physical extent(PE)**: 硬盘可供指派给逻辑卷的最小单位（通常为4MB）

## 命令代码

列出可被用作物理卷的设备

``` bash
# lvmdiskscan
```

创建物理卷

``` bash
# pvcreate DEVICE

e.g.
# pvcreate /dev/sda2
```

查看已创建好的物理卷

```bash
# pvdisplay
```

创建卷组

```bash
# vgcreate <volume_group> <physical_volume>

e.g.
# vgcreate Fedora /dev/sda2
```

让卷组包含其它物理卷

```bash
# vgextend <volume_group> <physical_volume>
# vgextend <volume_group> <another_physical_volume>

e.g.
# vgextend Fedora /dev/sdb1
# vgextend Fedora /dev/sdc
```

查看已创建卷组

```bash
# vgdisplay
```

创建逻辑卷

```bash
# lvcreate -L <size> <volume_group> -n <logical_volume>

e.g.
# lvcreate -L 10G Fedora -n lvroot
```

创建完逻辑卷后可以通过/dev/Fedora/lvroot或/dev/mapper/Fedora-lvroot来访问它

可以指定一个或多个物理卷来限制LVM分配数据空间的位置。比如希望在较小的SSD硬盘上创建根文件系统，并在较慢的机械硬盘上创建家目录卷，仅需把物理卷设备加入到命令中

```bash
# lvcreate -L 10G Fedora -n lvroot /dev/sdc1
```

让逻辑卷拥有卷组（VG）的所有未使用空间

```bash
# lvcreate -l +100%FREE <volume_group> -n <logical_volume>
```

查看已创建逻辑卷

```bash
# lvdisplay
```

逻辑卷创建完后可以像普通分区一样创建文件系统

移除逻辑卷

```bash
# lvremove <volume_group>/<logical_volume>
```

