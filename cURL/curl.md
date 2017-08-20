# CURL POST

```
#windows下需转译双引号

curl -H "Content-Type: application/json" -X POST -d "{\"name\": \"admin\", \"password\": \"admin\", \"remember\": \"true\"}" http://127.0.0.1:5000/login
```