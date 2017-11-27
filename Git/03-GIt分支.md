# 创建分支

```bash
$ git branch <branch_name>

-b 同时切换到新建的分支
```

# 分支切换

```bash
$ git checkout <branch_name>
```

# 合并分支

```bash
$ git merge <branch_name> #将<branch_name>合并到当前分支
```

# 删除分支

```bash
$ git branch -d <branch_name>
```

# 列出所有分支

```bash
$ git branch

-v 显示每一个分支最后一次提交
```

# 变基（清理提交历史）

只对尚未推送或分享给别人的本地修改执行变基操作清理历史，从不对已推送至别处的提交执行变基操作，

```bash
$ git rebase <branch_name> # 将当前分支变基到<branch_name>
````