# find

```bash
-name 按照文件名查找
find . -name '*.c'

-perm 按照文件权限查找
find . -perm 755

-user 按照文件所有者查找
find . -user hyperion

-group 按照文件所属的组查找
find . -group root

-mtime -n/+n 按照文件更改时间查找，-n表示更改时间距现在n天以内，+n更改时间剧现在n天以前
find . -mtime +7

-type 查找某一类型的文件
b 块设备文件
d 目录
c 字符设备
p 管道文件
l 符号链接文件
f 普通文件

-size n[cbkMG] 按文件大小查找 +表示大于，-表示小于

b 512字节默认单位
c 字节bytes
k 1024 bytes
M 
G 
```

# xargs

```bash
find . -size 0 | xargs rm -rf
```

# exec

```bash
find . -size 0 -exec rm -rf {} \;

考虑到分号在各个系统中会有不同的意义，所以前面加反斜杠
```
