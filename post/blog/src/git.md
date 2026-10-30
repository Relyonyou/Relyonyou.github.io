# Git 的操作

- 日期：2020-03-11

## 关于Git的一些操作

## 从本地上传文件到Github

1. 将本地文件添加到分支的项目中
2. 初始化本地仓库 ------ git init
3. 将本地内容添加至git本地暂存区中 -------git add .
4. 将暂存区的信息添加到本地仓库中 ------git commit -m "XXXX"
5. 添加远程仓库路径git remote add origin [https://github.com/xxxx/xxx.git](https://github.com/xxxx/xxx.git)
6. 将本地仓库的内容推到项目的master分支上去 -----git push -u origin master

## 提交PR到别人的项目中

1. 先将别人的仓库fork到自己的名下  
2. 然后将仓库克隆到本地(clone,将项目地址clone下来)  
git clone xxx  
3. 在本地修改代码  
支持markdown格式  
4. 提交代码到自己的GitHub的远程仓库(见上文)  
5. 提交PR  
![enter description here](/post/blog/img/git-1.webp)

![enter description here](/post/blog/img/git-2.webp)

## 解决冲突

## 先手动解决冲突的内容  
![enter description here](/post/blog/img/git-3.webp)

> Git用<<<<<<<，=======，>>>>>>>标记出不同分支的内容，然后我们根据情况，手动解决，然后再提交就可以了。
>
> 手动解决冲突后，执行以下命令：

```bash
git add contributions/USER_LIST.md
git rebase --continue
```

## 一些Git的常用命令

> **git clone url**：获取一个url对应的远程Git repo, 创建一个local copy
>
> **git add .** ：将工作区中所有未跟踪或者修改的文件添加到暂存区
>
> **git commit -m** "提交注释信息" ：将暂存区里的改动给提交到本地的版本库
>
> **git push origin master**：将本地的master分支推送到远程主机(缺省是origin名称，可以通过git  
> **remote**查询远程主机的别名)
>
> **git remote**:列出remote 别名。
>
> **git remote rm [别名**]: 删除一个存在的remote alias。
>
> **git remote set-url**[别名] [url]:更新远程repo的url。
>
> **git status**： 查询repo的状态。显示工作目录和暂存区的状态
>
> **git branch**： 列出本地所有分支,当前分支会被星号标示出。
>
> **git branch (branchname)**: 创建一个新的分支(当你用这种方式创建分支的时候,分支是基于你的上一次提交建立的)。
>
> **git checkout (branchname)**：切换到一个分支。
>
> **git config -l**：查看git config的信息
>
> **git push -f：强推（慎用**），即利用强覆盖方式用你本地的代码替代git仓库内的内容
>
> **git checkout -b branch-name** #"创建分支"
>
> **git checkout -- xxx/xxx.md** -------恢复文件
>
> **origin**：你自己fork出来的仓库，并通过clone到本地。此时你自己远程的仓库相对于你本地仓库就 origin。你可以随意向其提交（push）代码。
>
> **upstream**：远程（原始）仓库对于本地仓库来说，就是upstream。  
> 将本地仓库与上游仓库内容进行同步
>
> **git remote add upstream git@github.com:2020NCOV/ncov-report** -----添加upstream  
> **git fetch upstream master** ---使用fetch命令，先将远程upstream的内容同步到本地  
> **git rebase upstream/master** ---再将本地内容提交的github上自己的仓库中
>
> **git push origin --delete branch-name**---删除远程分支
>
> **git checkout master -f**---检出并切换本地仓库的主分支（master）：
>
> **git branch -D branch-name**----删除本地分支branch-name：
>
> **git pull --ff upstream master**---用最新的upstream版本来更新本地仓库的主分支（master）：

## Git使用vi或vim命令打开.关闭,保存文件

> 1、vi & vim 有两种工作模式：

（1） 命令模式：接受、执行 vi & vim 操作命令的模式，打开文件后的默认模式；

（2） 编辑模式：对打开的文件内容进行 增、删、改 操作的模式；

# 在编辑模式下按下 ESC 键，回退到命令模式。

> 2、创建、打开文件：$ vi 文件名

（1）使用 vi 加 文件路径（或文件名）的模式打开文件，如果文件存在则打开现有文件，如果文件不存在则新建文件，并在终端最下面一行显示打开的是一个新文件。

（2）键盘输入字母 “i”或“Insert”键进入最常用的插入编辑模式。

> 3、保存文件：

（1）在插入编辑模式下编辑文件。

（2）按下 “ESC” 键，退出编辑模式，切换到命令模式。

（3）在命令模式下键入"ZZ"或者":wq"保存修改并且退出 vi 。

（4）如果只想保存文件，则键入":w"，回车后底行会提示写入操作结果，并保持停留在命令模式。

> 4、放弃所有文件修改：

（1）放弃所有文件修改：按下 "ESC" 键进入命令模式，键入 ":q!" 回车后放弃修改并退出vi。

（2）放弃所有文件修改，但不退出 vi ，即回退到文件打开后最后一次保存操作的状态，继续进行文件操作：按下 "ESC" 键进入命令模式，键入 ":e!" ，回车后回到命令模式。

---
