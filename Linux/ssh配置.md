# ssh 配置

```
/etc/ssh/sshd_config
---------------------------
PermitRootLogin no  #禁止root用户登录
```

## 登陆显示信息

```
/etc/ssh/sshd_config
-------------------------
Banner path/to/msg/file
```