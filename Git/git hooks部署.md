# git hooks部署

## 服务器端初始化git裸仓库（相当于git服务端）

```bash
~/git/
---------------

$ git init --bare api.git
```

## 开发机本地建立git仓库

```bash
$ git init

$ git add .

$ git commit -a

$ git remote add deploy hyperion@127.0.0.1:~/git/api.git

$ git push deploy master
```

## 服务器创建非裸仓库

```
$ git clone ~/git/api.git 
```

## 编辑hooks文件

```
~/git/api.git/hooks/post-receive
----------------------------------
#!/bin/bash

unset GIT_DIR

cd /home/hyperion/api

echo "Pulling code"

git pull origin master

echo "Upload api code done"

exit 0
```



