# 安装

```bash
# dnf install tomcat tomcat-webpapps tomcat-admin-webapps
```

```
/usr/share/tomcat/tomcat-users.xml
-----------------------

<role rolename="admin"/>
<role rolename="admin-gui"/>
<role rolename="admin-script"/>
<role rolename="manager"/>
<role rolename="manager-gui"/>
<role rolename="manager-script"/>
<role rolename="manager-jmx"/>
<role rolename="manager-status"/>
<user name="admin" password="dongjj" roles="admin,manager,admin-gui,admin-script,manager-gui,manager-script,manager-jmx,manager-status" /> 
```
