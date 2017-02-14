# LVM

LVM利用Linux内核的device-mapper来实现存储系统的虚拟化（系统分区独立于底层硬件）。 通过LVM，你可以实现存储空间的抽象化并在上面建立虚拟分区（virtual partitions），可以更简便地扩大和缩小分区，可以增删分区时无需担心某个硬盘上没有足够的连续空间

## LVM基本组成

1. **物理卷Physical volume(PV)**: 可以在上面建立卷组的媒介，可以是硬盘分区，也可以是硬盘本身或者回环文件（loopback file）

2. **卷组Volume group(VG)**: 将一组物理卷收集为一个管理单元。

3. **逻辑卷Logical volume(LV)**: 虚拟分区，由物理区域（physical extents）组成

4. **物理区域Physical extent(PE)**: 硬盘可供指派给逻辑卷的最小单位（通常为4MB）

## 命令代码


``` bash
# 列出可被用作物理卷的设备

# lvmdiskscan
```
