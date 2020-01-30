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

1. 用户加密认证

用户密码加密存储，使用MD5加密
    
2. 允许多用户登录
3. 每个用户都有自己的家目录，且只能访问自己的家目录

数据库中有多用户信息

文件传输目录有多用户目录

每次用户登录都在自己的家目录

通过认证的用户设置动态设置当前目录

4. 对用户进行磁盘分配，每一个用户的可用空间可以自己设置

定义一个函数，计算用户目录下所有文件的总大小

每次接收文件之前计算当前可用空间减去要接收文件的大小是否还存在可用可用，如有则接收，否则返回空间不足消息

5. 允许用户在ftp server上随意切换目录

通过cd命令可以动态更改当前用户的当前目录

6. 允许用户查看自己家目录下的文件

通过ls命令获取当前用户当前目录的文件信息，返回给客户端

7. 允许用户上传和下载，保证文件的一致性（md5）

定义一个校验函数，每次收发文件之前校验文件一致性

发送文件时，先将文件内容进行MD5加密，然后发送文件内容和MD5值

接收文件时，先将文件内容接收到内存中，计算MD5值，将计算结果与接收的MD5值对比，如一致则将文件写入本地，否则返回文件不完全信息

8. 文件上传、下载过程中显示进度条

通过tqdm库显示进度条

9. 文件支持断点续传

通过在客户端接收文件时记录日志判断文件是否接收完毕

## 应用通用信息定义

#### Server端

accounts.ini
用户个人信息结构：

    [Nickname]
    name=Nickname
    password=MD5 encryption
    total_space=Total space available to users
    used_space=User used space

#### Client端

用户指令列表：
    
    get         从服务器下载文件
    
    put         上传文件到服务器
    
    ls          显示当前目录文件及文件夹
    
    cd          更改目录
    
    cp          文件或文件夹复制
    
    mv          文件或文件夹移动
    
    re          文件或文件夹重命名
    
    mkdir       创建文件夹
    
用户登录格式：

python3 client.py -s localhost -P port -u username -p password

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

    720: "Catalog changed.",                # 客户端请求更改目录时，如果目录存在，返回目录更改成功
    721: "Directory does not exist.",       # 客户端请求更改目录时，如果目录不存在，返回给用户目录不存在

    730: "Folder created successfully.",    # 文件夹创建成功
    731: "Folder already exists.",          # 文件夹已存在

    740: "Replication success.",            # 文件或文件夹复制成功
    
    750: "Rename successful.",                               # 文件或文件夹重命名成功
    751: "Rename failed， file or folder already exists",    # 文件或文件夹已存在，重命名失败
}
```