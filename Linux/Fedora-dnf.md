# Fedora包管理器DNF

查看dnf包管理器版本

```bash
# dnf --version
```

查看系统中可用的DNF软件库

```bash
# dnf repolist
```

查看系统中可用和不可用的所有DNF软件库

```bash
# dnf repolist all
```

列出所有RPM包

```bash
# dnf list
```

列出所有安装了的RPM包

```bash
# dnf list installed
```

列出所有可供安装的RPM包

```bash
dnf list available
```

搜索软件库中的RPM包

```bash
# dnf search <packname>
```

查找某一文件的提供者

```bash
# dnf provides /bin/bash
```

查看软件包详情

```bash
# dnf info <packname>
```

安装软件包

```bash
# dnf install <packname>
```

升级软件包

```bash
# dnf update <packname>
```

检查系统软件包的更新

```bash
# dnf check-update
```

升级所有系统软件包

```bash
# dnf update

或者

# dnf upgrade
```

删除软件包

```bash
# dnf remove <packname>

或者

# dnf erase <packname>
```

删除无用孤立的软件包

```bash
# dnf autoremove
```

删除缓存的无用软件包

```bash
# dnf clean all
```

查看dnf命令的执行历史

```bash
# dnf history
```

查看所有的软件包组

```bash
# dnf grouplist
```

安装一个软件包组

```bash
# dnf groupinstall <groupname>
```

升级一个软件包组中的软件

```bash
# dnf groupupdate <groupname>
```

删除一个软件包组

```bash
# dnf groupremove <groupname>
```

