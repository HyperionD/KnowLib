# Bower 学习

## 安装

```
$ npm install -g bower
```

bower依赖node, npm, git

## 安装包

使用 `bower install` 安装包, bower会将包安装到bower_components/目录下

```
$ bower install <package>
```
```
# 安装bower.json中列出项目依赖的包
$ bower install

# registered package
$ bower install jquery

# Github shortHadn
$ bower install desandro/masonry

# Git endpoint
$ bower install git://github.com/user/package.git

# url
$ bower install http://example.com/script.js

# 指定版本
$ bower install <package>#<version>
```

## 搜索包

```
$ bower search <query>
```

## bower.json

```
# 创建bower.json
$ bower init

# 将安装的包写入bower.json
$ bower install <package> --save
```

## 列出以安装的包

```
$ bower list
```

## 更新包

```
$ bower update <package>

# 更新所有bower.json中的包
$ bower update
```

## .bowerrc 文件

```
{
  "directory": "path/to/package/directory"
}
```
