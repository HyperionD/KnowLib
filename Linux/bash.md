# 输入输出重定向

## 文件描述符

0	标准输入	    stdin	键盘
1	标准输出	    stdout	屏幕
2	标准错误输出	stderr	屏幕

## 文件描述符重定向

```bash
$ cmd >&n 把输出送到文件描述符n

$ cmd 2>file 把文件描述符2重定向到file，即把错误输出存到file中
$ cmd > file 2>&1 把标准错误重定向到标准输出，再重定向到file，即stderr和stdout都被输出到file中
$ cmd &> file	功能与上一个相同，更为简便的写法
$ cmd >& file	功能仍与上一个相同。
$ cmd > f1 2>f2	把stdout重定向到f1，而把stderr重定向到f2
```

## time 输出重定向

time 将结果输出到stderr

```bash
$ (time cmd > /dev/null) 2>&1 | grep real |awk '{print $2}'
```
