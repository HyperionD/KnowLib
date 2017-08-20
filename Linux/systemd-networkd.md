# 使用systemd-networkd设置网络

## 静态IP

```
/etc/systemd/network/<yournet>.network
---------------------------------------------

[Match]
Name=enp0s3

[Network]
Address=192.168.1.200/24
Gateway=192.168.1.1
```

## dhcp

```
/etc/systemd/network/<yournet>.network
---------------------------------------------

[Match]
Name=enp0s3

[Network]
DHCP=ipv4

[DHCP]
RouteMetric=10
```