# FTP在线文件传输系统

## 基础需求

1. 用户加密认证

2. 允许多用户登录

3. 每个用户都有自己的家目录，且只能访问自己的家目录

4. 对用户进行磁盘分配，每一个用户的可用空间可以自己设置

5. 允许用户在ftp server上随意切换目录

6. 允许用户查看自己家目录下的文件

7. 允许用户上传和下载，保证文件的一致性（md5）

8. 文件上传、下载过程中显示进度条

## 升级需求

1. 文件支持断点续传


## 需求分析

用户加密认证

    
    用户密码加密存储，使用MD5加密
    
允许多用户登录
每个用户都有自己的家目录，且只能访问自己的家目录

    
    数据库中有多用户信息
    
    文件传输目录有多用户目录

    每次用户登录都在自己的家目录
    
    通过认证的用户设置动态设置当前目录

对用户进行磁盘分配，每一个用户的可用空间可以自己设置


    定义一个函数，计算用户目录下所有文件的总大小
    
    每次接收文件之前计算当前可用空间减去要接收文件的大小是否还存在可用可用，如有则接收，否则返回空间不足消息

允许用户在ftp server上随意切换目录

    
    通过cd命令可以动态更改当前用户的当前目录

允许用户查看自己家目录下的文件

    
    通过ls命令获取当前用户当前目录的文件信息，返回给客户端

允许用户上传和下载，保证文件的一致性（md5）


    定义一个校验函数，每次收发文件之前校验文件一致性
    
    发送文件时，先将文件内容进行MD5加密，然后发送文件内容和MD5值
    
    接收文件时，先将文件内容接收到内存中，计算MD5值，将计算结果与接收的MD5值对比，如一致则将文件写入本地，否则返回文件不完全信息

文件上传、下载过程中显示进度条

    
    通过tqdm库显示进度条

文件支持断点续传

    
    通过在客户端接收文件时记录日志判断文件是否接收完毕
    
    服务端根据客户端已经接收的数据seek到指定位置继续传输

## 应用通用信息定义

#### Server端

服务端发送消息形式：

```python
server_message = 
    "status_code": status_code,
    "status_message": "status message",
    "fill": "Missing fill",
    
    "file_path": The path of the file on the server,
    "file_size": Size of transfer file,
    "file_MD5": File MD5 value,
}
```

accounts.ini
用户个人信息结构：

    [Nickname]
    name=Nickname
    password=MD5 encryption
    total_space=Total space available to users
    used_space=User used space

#### Client端

客户端发送消息形式：

```python
client_message = 
    "instruction_type": "Instruction type",
    "fill": "Missing fill",

    "file_size": Size of transfer file,
    "file_MD5": File MD5 value,
}
```

客户端指令列表：
    
    get         从服务器下载文件
    
    put         上传文件到服务器
    
    ls          显示当前目录文件及文件夹
    
    cd          更改目录
    
    cp          文件或文件夹复制
    
    mv          文件或文件夹移动
    
    rm          删除文件或文件夹
    
    mkdir       创建文件夹
    
#### Server-Client交互状态码及信息

```python
STATUS_CODE = {
    700: "Pass password verification.",     # 用户密码验证通过
    701: "User name does not exist.",       # 用户名不存在
    702: "Password error",                  # 密码错误
    710: "File exists.",                        # 客户端请求下载文件时，服务端存在此文件
    711: "File does not exist.",                # 客户端请求下载文件时，服务端不存在此文件
    712: "File size and MD5 values.",           # 客户端请求下载文件时，如果服务端存在此文件，先返回文件大小和MD5值
    713: "Resend file size and MD5 value.",     # 客户端请求重新下载文件时，如果服务端还存在此文件，返回文件大小和MD5值
    714: "MD5 value not match.",                # 客户端请求重新下载文件时，文件MD5值不一致
    720: "Catalog changed.",                # 客户端请求更改目录时，如果目录存在，返回目录更改成功
    721: "Directory does not exist.",       # 客户端请求更改目录时，如果目录不存在，返回给用户目录不存在
    722: "Beyond access",                   # 客户端请求更改的目录超出访问权限
    730: "Folder created successfully.",    # 文件夹创建成功
    731: "Folder already exists.",          # 文件夹已存在
    740: "Success.",                                    # 文件或文件夹复制或移动成功
    741: "Original file or folder does not exist",      # 原文件或文件夹不存在
    742: "Target file or folder already exists",        # 目标文件或文件夹已存在
    743: "Path exceeds access rights",                  # 路径超出访问权限
    750: "Rename successful.",                               # 文件或文件夹重命名成功
    751: "Rename failed， file or folder already exists",    # 文件或文件夹已存在，重命名失败
    760: "Message size",            # 消息的大小
    770: "Remove file or folder successfully."      # 删除文件或文件夹成功
}
```

## 程序启动方式

程序需要第三方库安装：

pip install tqdm

服务端启动指令：

python3 server.py start

python3 server.py creat_user

客户端启动指令：

python3 client.py -s localhost -p port

## 程序运行效果

#### 服务器管理员创建用户

```
python3 server.py creat_user
Please input user nickname: Alex
Please input user password: 20001001
Please input user total space: 500M

python3 server.py creat_user
Please input user nickname: Coco
User already exited!

python3 server.py creat_user
Please input user nickname: Coco
Please input user password: 20001116
Please input user total space: 500M
```

```ini
[Alex]
name = Alex
password = 890cf2618151e20144c46753beedef3c
total_space = 500M
used_space = 0

[Coco]
name = Coco
password = 1e85b303b617b76f8d0538dcd5ffe31f
total_space = 500M
used_space = 0
```

#### 客户端基本指令演示

```
python3 client.py -s localhost -p 9999
Please input username: Alex
Please input password: 20001001
[Alex]>>> ls
 驱动器 G 中的卷是 Code
 卷的序列号是 AC81-1911

 G:\Python\PythonFullStack\第三模块_面向对象+网络编程基础\作业\支持多用户在线的FTP程序\server\home\Alex 的目录

2020/01/31  12:01    <DIR>          .
2020/01/31  12:01    <DIR>          ..
2020/01/27  08:53           674,452 file0.pdf
2020/01/31  12:01    <DIR>          images_test
2020/02/01  15:24    <DIR>          video_test
               1 个文件        674,452 字节
               4 个目录 92,718,886,912 可用字节

[Alex]>>> cd images_test
[Alex\images_test]>>> ls
 驱动器 G 中的卷是 Code
 卷的序列号是 AC81-1911

 G:\Python\PythonFullStack\第三模块_面向对象+网络编程基础\作业\支持多用户在线的FTP程序\server\home\Alex\images_test 的目录

2020/01/31  12:01    <DIR>          .
2020/01/31  12:01    <DIR>          ..
2020/01/24  12:52         1,231,222 兰博基尼0.jpg
               1 个文件      1,231,222 字节
               2 个目录 92,718,886,912 可用字节

[Alex\images_test]>>> cd ..
[Alex]>>> cd ..
Beyond access
[Alex]>>> cp file0.pdf file1.pdf
Replication success.
[Alex]>>> ls
 驱动器 G 中的卷是 Code
 卷的序列号是 AC81-1911

 G:\Python\PythonFullStack\第三模块_面向对象+网络编程基础\作业\支持多用户在线的FTP程序\server\home\Alex 的目录

2020/02/01  15:30    <DIR>          .
2020/02/01  15:30    <DIR>          ..
2020/01/27  08:53           674,452 file0.pdf
2020/02/01  15:30           674,452 file1.pdf
2020/01/31  12:01    <DIR>          images_test
2020/02/01  15:24    <DIR>          video_test
               2 个文件      1,348,904 字节
               4 个目录 92,718,211,072 可用字节

[Alex]>>> mkdir file_test
Folder created successfully.
[Alex]>>> mv file0.pdf file_test
Replication success.
[Alex]>>> rm file0.pdf
Original file does not exist
[Alex]>>> rm file1.pdf
Remove file or folder successfully.
```

#### 客户端上传、下载、断点续传功能

```
python3 client.py -s localhost -p 9999
Please input username: Alex
Please input password: 20001001
[Alex]>>> cd video_test
[Alex\video_test]>>> get video0.mp4
Progressing: 1556480: : 0it [00:00, ?it/s]
---File [video0.mp4] received done, received size [1558638]----
[Alex\video_test]>>> put video1.mp4
Progressing: 6798273: : 0it [00:01, ?it/s]
----------------File upload done.-----------------
[Alex\video_test]>>> get video1.qsv
Progressing: 6463488: : 0it [00:01, ?it/s]
Process finished with exit code -1
```
```
python3 client.py -s localhost -p 9999
Please input username: Alex
Please input password: 20001001
---------------Unfinished file list---------------
video1.qsv    100.00%    \video_test    7f79a6b61efd3a4d574b8efd98a93ad3
Select filename to re-download (q to quit): video1.qsv
Server resend file:  video1.qsv
Progressing: 224038848: : 0it [00:09, ?it/s]File [video1.qsv] received done, received size [224039404]
Select filename to re-download (q to quit): quit
[Alex]>>> quit
Ftp client stop.
```