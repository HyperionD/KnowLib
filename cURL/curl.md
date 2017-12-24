# CURL POST

```bash
#windows下需转译双引号

curl -H "Content-Type: application/json" -X POST -d "{\"name\": \"admin\", \"password\": \"admin\", \"remember\": \"true\"}" http://127.0.0.1:5000/login
```


# windows下解决curl: (60) SSL certificate problem: unable to get local issuer certificate

1. 下载[cacert.pem](https://curl.haxx.se/ca/cacert.pem)
2. 设置环境变量CURL_CA_BUNDLE = /path/to/cacert.pem

