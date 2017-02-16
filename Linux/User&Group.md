# User相关

## 新建用户

```bash
# useradd -m -g <初始组> -G <附加组> -s <登陆shell> <用户名>

-g: 如果没有设置会根据/etc/login.defs文件中的USERGROUPS_ENAB环境变量进行设置。默认（USERGROUPS_ENAB yes）会用和用户名相同的名字创建群组，GID等于UID

-G: 使用逗号分隔多个组，如果不设置用户仅加入初始组
```

## 更改用户登录名

```bash
# usermod -l <newname> <oldname>
```

## 更改用户主目录

```bash
# usermod -d </my/new/home> -m <username>
```

## 将用户加入群组

```bash
# usermod -aG <Group> <username>

用逗号分隔
```

## 删除用户

```bash
# userdel -r <username>

-r: 一并删除用户主目录和邮件
```

# Group相关

## 新建组

```bash
# groupadd <groupname>
```
