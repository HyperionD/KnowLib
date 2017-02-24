# MySQL

## 初始化 mysql_install_db

datadir不能位于/home下，默认为/var/lib/mysql

```bash
# mkdir /data
# chown mysql.mysql /data
# mysql_install_db --user=mysql --basedir=/usr --datadir=/data

在/etc/mysql/my.cnf中的[mysqld]段中添加datadir=<YOUR_DATADIR>

# systemctl start mysqld
# mysql_secure_installation
# systemctl restart mysqld
```

## 查看datadir目录位置

```mysql
mysql> show variables like 'datadir';
```

# 新建用户

```mysql
mysql> create user 'username'@'hostname' identified by 'password';
mysql> grant all privileges on *.* to 'username'@'hostname';
mysql> flush privileges;
mysql> quit
```
