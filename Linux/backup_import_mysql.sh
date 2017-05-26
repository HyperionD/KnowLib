#!/bin/bash

# create db_dir if not exist
db_dir=$HOME/db
if [ ! -d "$db_dir" ]; then
  mkdir "$db_dir"
fi

sql_file=amazon_remote_db_`date +%F`.sql.gz
sql_path=$db_dir/$sql_file
backup_log_file=$db_dir/backup.log

# backup from amazon remote db
backup_start=`date "+%F %T"`
backup_time=`(time mysqldump -uroot -pdongjj --quick --single-transaction --add-drop-table --databases test | gzip > $sql_path) 2>&1 |grep real |awk '{print $2}'`
backup_log='Backup DB at '$backup_start' Use '$backup_time
echo "" >> $backup_log_file
echo $backup_log >> $backup_log_file

# import remote db to local mysql db
import_start=`date "+%F %T"`
import_time=`(time gunzip < $sql_path | mysql -h localhost -uroot -pdongjj) 2>&1 |grep real | awk '{print $2}'`
import_log="Import DB at "$import_start" Use "$import_time
echo $import_log >> $backup_log_file
