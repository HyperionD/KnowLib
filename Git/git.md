# 初始化操作

``` bash
$ git config --global user.name "HyperionD"

$ git config --global user.email "dongjj81@gmail.com"

$ ssh-keygen

# 仅windows下操作

$ git config --global core.autocrlf false
```

# 一次推送多个远程仓库

使用命令

``` bash
$ git remote set-url --add origin git-url
```

或者在.git/config文件[remote "origin"]节点下手动添加url
