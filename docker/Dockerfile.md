# Dockerfile 文件

```
FROM <image> 

指定基础镜像, scratch表示空白镜像
``` 

```
RUN <command> 

执行命令
```

```
COPY <源路径> <目标路径> 

复制文件 源路径为构建上下文目录 

目标路径为新一层镜像内的路径，没有会自动创建
```

```
ADD  

同COPY 但是会自动解压gzip, bzip2, xz压缩文件
```

```
CMD ["可执行文件", "参数1", "参数2"] 

容器启动命令
```

```
ENTRYPOINT

同CMD命令，当指定ENTRYPOINT时，

CMD内容会作为ENTRYPOINT的参数
```

```
ENV <key1=value1> <key2=value2> 

设置环境变量
```

```
VOLUME ["<路径1>", "<路径2>"]

VOLUME <路径>

定义匿名卷
```

```
EXPOSE <端口1> <端口2>...

声明端口，仅声明容器打算使用什么端口，

并不会自动在宿主机进行端口映射
```

```
WORKDIR <工作目录路径>

指定工作目录（当前目录），不存在会自动建立
```

```
USER <用户名>

指定当前用户
```



