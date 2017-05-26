# 显示支持的zone

```bash
# firewall-cmd --get-zones
```

# 设置默认zone

```bash
# firewall-cmd --set-default-zone=<zone>
```

# 查看当前的zone

```bash
# firewall-cmd --get-active-zones
```

# 显示所有公共区域

```bash
# firewall-cmd --zone=public --list-all
```

# 显示服务列表

```bash
# firewall-cmd --get-services
```

# 显示当前服务

```bash
# firewall-cmd --list-services
```

# 允许服务通过

```bash
# firewall-cmd --enable service=ssh
```

# 将服务加入到zone

```bash
# firewall-cmd --zone=<zone> --add-service=<service>
```

# 服务从zone移除

```bash
# firewall-cmd --zone=<zone> --remove-service=<service>
```

# 重新加载配置

```bash
# firewall-cmd --reload
```

# 查看zone端口开放情况

```bash
# firewall-cmd --zone=<zone> --list-port
```

# 打开端口

```bash
sudo firewall-cmd --zone=<zone> --add-port=8080/tcp --permanent

--zone 作用域
--add-port=8080/tcp 端口/通讯协议
--permanent 永久生效

sudo firewall-cmd --reload
```
