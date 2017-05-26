# binlog

```
# /etc/my.cnf
----------------

[mysqld]
# binlog文件的前缀，例如fedora-bin.000001, fedora-bin.000002
log-bin=fedora-bin 

# binlog index文件的名称
log-bin-index=fedora-bin.index
```

# 显示binlog配置信息

```mysql
mysql> show variables like '%log_bin%';
```

# 查看所有binlog日志列表

```mysql
mysql> show master logs;
```

# 刷新日志，产生一个新编号的binlog日志

```mysql
mysql> flush logs;
```

# 清空所有日志

```mysql
mysql> reset master;
```
