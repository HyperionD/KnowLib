# apache虚拟主机配置

## 启用vhost

取消配置文件中的注释

```
/etc/httpd/conf/httpd.conf
--------------------------
# Include conf/extra/httpd-vhosts.conf
```

## 编辑 extra/httpd-vhosts.conf 文件

```
<VirtualHost *:80>
    #ServerAdmin webmaster@dummy-host.example.com
    DocumentRoot "/srv/http/site2"
    ServerName localhost
    #ServerAlias www.dummy-host.example.com
    #ErrorLog "/var/log/httpd/dummy-host.example.com-error_log"
    #CustomLog "/var/log/httpd/dummy-host.example.com-access_log" common
</VirtualHost>

<VirtualHost *:7777>
    #ServerAdmin webmaster@dummy-host2.example.com
    DocumentRoot "/srv/http/vue"
    ServerName localhost:7777
    #ErrorLog "/var/log/httpd/dummy-host2.example.com-error_log"
    #CustomLog "/var/log/httpd/dummy-host2.example.com-access_log" common
    <Directory "/src/http/vue">
      DirectoryIndex index.html
    </Directory>
</VirtualHost>

```

## 编辑http.conf添加监听的端口

```
/etc/httpd/conf/httpd.conf
-----------------------------

Listen 80
LIsten 7777

```

