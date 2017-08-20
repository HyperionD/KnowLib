# PHP

## 安装PHP

```bash
# pacman -S php-fpm
```

## 编辑 /etc/nginx/nginx.conf

```
/etc/nginx/nginx.conf
-------------------------------

location ~ \.php$ {
            root           /usr/share/nginx/html;
            fastcgi_pass   unix:/run/php-fpm/php-fpm.sock;
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
            include        fastcgi_params;
}
```

## 编写测试php

```
test.php
-------------------
<?php
  phpinfo();
?>
```

## 启动php服务

```bash
# systemctl start php-fpm

# systemctl enable php-fpm
```

## 启用PHP扩展

取消以下注释

```bash
/etc/php/php.ini
----------------------

;extension=mysqli.so
;extension=pdo_mysql.so

-------------------------

# systemctl reload php-fpm
```