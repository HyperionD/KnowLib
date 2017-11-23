# 镜像相关命令

## docker run 

```
# docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

# docker run -it --rm centos bash

[OPTIONS]
-i 开启准输入

-t 终端

-d 容器在后台运行

-e 设定环境变量

-p <host_port>:<container_ip> 映射端口

--name 为容器指定名字

--rm 容器退出后随之将其删除
```

## 列出镜像

```bash
# docker images

# docker image ls
```

## 构建镜像

```bash
# docker build [选项] <上下文路径/URL/->
```

## 删除镜像

```bash
# docker rmi [选项] <镜像>
```

# 容器相关命令

## 启动已终止的容器

```bash
# docker start

# docker container start
```

## 终止容器

```bash
# docker stop
```

## 进入容器

```bash
# docker attach
```

## 删除容器

```bash
# docker rm
```

# 卷相关命令

## 列出卷

```bash
# docker volume ls
```

## 删除卷

```bash
# docker vloume rm
```
