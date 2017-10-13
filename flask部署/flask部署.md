# flask部署

## nginx 配置

```
/etc/nginx/nginx.conf
-------------------------
server {
        listen 8000;
        server_name localhost;
        charset utf-8;
        location /{
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            #proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   Host      $http_host;
            proxy_redirect off;
            proxy_pass http://127.0.0.1:8001; #gunicorn 端口
        }
    }
```

## 配置gunicorn使用systemd管理

```
/etc/systemd/system/gunicorn.service
------------------------------------------
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
PIDFile=/run/gunicorn/pid
User=hyperion
Group=hyperion
RuntimeDirectory=gunicorn
WorkingDirectory=/home/hyperion/api
ExecStart=/usr/bin/gunicorn -w 3 -b 127.0.0.1:8001 -u hyperion --pid /home/hyperion/nginx/gunicorn.pid api:app
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```