# NextCloud 安装 （参考 https://www.linuxbabe.com/cloud-storage/nextcloud-server-arch-linux-nginx-mariadb-php7）

## 安装 PHP

见php记录

## 安装mariadb

见mysql记录

## 创建nextcloud数据库

```bash
# msyql -u root -p 
```

```mysql
create database nextcloud;

create user nextclouduser@localhost identified by 'your-password';

grant all privileges on nextcloud.* to nextclouduser@localhost identified by 'your-password';

flush privileges;

exit;

```