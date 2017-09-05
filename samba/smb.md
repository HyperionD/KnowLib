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

## firewalld配置

```bash
# firewall-cmd --permanent --add-service=samba

# firewall-cmd --reload
```

## selinux配置

```bash
# semanage fcontext -a -t samba_share_t "/bak01(/.*)?"

# restorecon -R -v /bak01

---------------------------------------------------------
ntfs格式分区不支持selinux需要在fstab中加入：

context=system_u:object_r:samba_share_t:s0
```

