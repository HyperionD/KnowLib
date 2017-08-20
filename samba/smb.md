# samba

## 配置文件位置

/etc/samba/samba.conf


## 添加samba用户

用户必须在系统系统中存在

```bash
# smbpasswd -a hyperion
```

## 启用用户

```bash
# smbpasswd -e hyperion
```

## 启动服务

```bash
# systemctl start smbd
# systemctl start nmbd
# systemctl enable smbd
# systemctl enable nmbd
```

## 测试配置文件

```bash
# testparm
```

