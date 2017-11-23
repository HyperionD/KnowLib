# Git 基础

## 初始化仓库

```bash
$ git init
```

## 克隆现有仓库

```bash
$ git clone <url>
```

## 查看当前文件状态

```bash
$ git status
```

## 状态简览

```bash
$ git status -s
```

## 跟踪新文件/添加内容到下一次提交中（暂存）

```bash
$ git add <file> 
```

## 忽略文件

.gitignore 文件中编辑不需要跟踪的文件

## 提交更新

```bash
$ git commit -m <message>
```

## 跳过使用暂存区

```bash
$ git commit -a
```

## 从git仓库中移出，仍保留在磁盘上

```bash
$ git rm --cached <file>
```

## 文件移动(重命名)

```bash
$ git mv <file_from> <file_to>
```

## 查看提交历史

```bash
$ git log
```

## 撤销对文件的修改

```bash
$ git checkout -- <file>
```

# 远程操作

## 查看远程仓库

```bash
$ git remote

$ git remote -v

$ git remote show <remote-name>
```

## 添加远程仓库

```bash
$ git remote add <shortname> <url>
```

## 从远程仓库中抓取与拉取

```bash
$ git fetch <remote-name> #不会自动合并到当前工作，需手动合并

$ git pull <remote-name> #自动抓取然后合并远程分支到当前分支
```

## 推送到远程仓库

```bash
$ git push <remote-name> <branch-name>
```

## 远程仓库重命名

```bash
$ git remote rename <old_remote_name> <new_remote_name>
```

## 移除远程仓库

```bash
$ git remote rm <remote-name>
```

# 打标签

## 列出标签

```bash
$ git tag
```

## 附注标签

```bash
$ git tag -a <tag_name> -m <message>
```

## 轻量标签

```bash
$ git tag <tag_name>
```

## 推送标签到远程仓库

```bash
$ git push <remote-name> <tag_name>

$ git push <remote-name> --tags  #将所有标签推送到远程仓库
```