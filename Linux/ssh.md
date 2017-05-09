# ssh 本地端口转发

```bash
ssh -f -C -N -L <local_port>:<remote_host/ip>:<remote_port> <user>@<host/ip>

-f 后台运行
-C 使用压缩功能
-N 不执行远程命令

<user>@<host/ip> 为可以连接到<remote_host/ip>的主机，作为中转
```
