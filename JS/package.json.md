# package.json

name: 项目名

version: 项目的版本号

description: 项目的描述

keywords: 项目简介

homepage: 项目官网的url

bugs: 项目提交问题的url和（或）邮件地址

license: 项目使用的协议

author: 项目的作者，可以是字符串或对象

contributors: 项目的贡献者，是一个数组

files: 项目中包含的所有文件，可取值为文件夹，.npmignore来去除不想包含到项目中的文件

main: 项目的入口文件

bin: 将项目中的可执行文件包含到系统PATH中

man: 指定一个单一文件或一个文件数组供man程序使用

scripts: 指定了运行脚本命令的npm命令行缩写

dependencies: 指定项目运行时依赖的模块

devDependencies: 项目开发时所需要的模块
```
version:  完全和version一致
>version: 必须比version大
>=version
<version
<=version
~version: 大概匹配version
^version: 兼容version
1.2.x
*:        任何版本都可以
```

engines: 指定项目运行环境

os： 指定项目的运行操作平台
