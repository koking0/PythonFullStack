#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/28 9:49
# @File     : ftp_client.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import os
import json
import tqdm
import socket
import hashlib
import optparse


class FtpClient:
    """Ftp客户端"""

    MSG_SIZE = 1024

    def __init__(self):
        self.username = None
        self.current_dir = None
        self.terminal_display = None
        self.log_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                                  "log"), "file.txt")

        # 处理参数
        parser = optparse.OptionParser()
        parser.add_option("-s", "--server", dest="server", help="ftp server ip address")
        parser.add_option("-p", "--port", type="int", dest="port", help="ftp server port")
        self.options, self.args = parser.parse_args()
        self.argv_verification()

        # 建立链接
        self.sock = None
        self.make_connection()

    def argv_verification(self):
        """检查参数合法性"""
        if not self.options.server or not self.options.port:
            exit("Error: must supply server and port parameters!")

    def make_connection(self):
        """建立socket链接"""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.options.server, self.options.port))

    def interactive(self):
        """处理与FtpServer的所有交互"""
        if self._auth():
            self.unfinished_file_check()
            while True:
                user_input = input(self.terminal_display).strip()
                if user_input == "quit":
                    exit("Ftp client stop.")
                if not user_input:
                    continue
                cmd_list = user_input.split()
                if hasattr(self, "_%s" % (cmd_list[0])):
                    func = getattr(self, "_%s" % (cmd_list[0]))
                    func(cmd_list[1:])

    def _auth(self):
        """用户认证"""
        count = 0
        while count < 3:
            count += 1
            username = input("Please input username: ").strip()
            password = input("Please input password: ").strip()
            if not username or not password:
                print("Username or password is empty.")
                continue

            self.send_msg(action_type="auth", username=username, password=password)
            response = self.get_response()
            if response.get("status_code") == 700:
                self.current_dir = "\\"
                self.username = username
                self.terminal_display = "[%s]>>> " % self.username
                return True
            else:
                print(response.get("status_msg"))
                return False

    def unfinished_file_check(self):
        """检查文件传输日志，把没正常接收完的文件列表打印，按用户的指令决定是否重传"""
        with open(self.log_path, "r") as file:
            file_list = file.readlines()
        unfinished_list = []
        for item in file_list:
            file = item.split(",")
            file[1] = int(file[1])
            if file[4] == "False":
                if not unfinished_list:
                    print("Unfinished file list".center(50, "-"))
                download_path = "%s\%s.download" % (os.path.dirname(os.path.abspath(__file__)), file[0])
                recv_size = os.path.getsize(download_path)
                file[1] = recv_size
                print("%s    %.2f%%    %s    %s" % (file[0], ((recv_size / file[1]) * 100), file[2], file[3]))
                unfinished_list.append(file)
        while unfinished_list:
            choice = input("Select filename to re-download (q to quit): ").strip()
            if choice == "q" or choice == "quit":
                break
            if not choice:
                continue
            for index, file in enumerate(unfinished_list) :
                if choice == file[0]:
                    print("Server resend file: ", file[0])
                    self.send_msg("re_get", filename=file[0], recv_size=file[1], file_path=file[2], file_md5=file[3])
                    response = self.get_response()
                    if response.get("status_code") == 713:
                        received_size, total_size = file[1], response.get("file_size")
                        temp_path = "%s\%s.download" % (os.path.dirname(os.path.abspath(__file__)), file[0])
                        f = open(temp_path, "ab")
                        progress_bar = tqdm.tqdm(total_size)
                        while received_size < total_size:
                            data = self.sock.recv(total_size - received_size if total_size - received_size < 8192 else 8192)
                            progress_bar.set_description("Progressing: %s" % received_size)
                            received_size += len(data)
                            f.write(data)
                        else:
                            print("File [%s] received done, received size [%s]" % (file[0], total_size))
                            f.close()
                            try:
                                os.rename(temp_path, "%s" % file[0])
                            except FileExistsError:
                                print("Local file already exist!")
                            with open(self.log_path, "r") as file_update:
                                file_list = file_update.readlines()
                            for index, file_item in enumerate(file_list):
                                temp = file_list[index].split(",")
                                if temp[0] == choice:
                                    file_list[index] = file_list[index].replace("False", "True")
                            with open(self.log_path, "w") as file_update:
                                for item in file_list:
                                    file_update.write(item)
                    else:
                        print(response.get("status_msg"))

    def _ls(self, cmd_args):
        self.send_msg(action_type="ls")
        response = self.get_response()

        if response.get("status_code") == 760:
            res, recv_size, res_size = b"", 0, response.get("result_size")
            while recv_size < res_size:
                data = self.sock.recv(res_size - recv_size if res_size - recv_size < 8192 else 8192)
                recv_size += len(data)
                res += data
            else:
                print(res.decode("gbk"))

    def _cd(self, cmd_args):
        """change to target dir"""
        if self.parameter_check(cmd_args, exact_args=1):
            self.send_msg("cd", target_dir=cmd_args[0])
            response = self.get_response()
            if response.get("status_code") == 720:
                self.current_dir = response.get("current_dir")
                self.terminal_display = "[%s%s]>>> " % (self.username, self.current_dir)
            else:
                print(response.get("status_msg"))

    def _cp(self, cmd_args):
        """copy file or folder"""
        if self.parameter_check(cmd_args, exact_args=2):
            self.send_msg("cp", original_path=cmd_args[0], target_path=cmd_args[1])
            response = self.get_response()
            print(response.get("status_msg"))

    def _mv(self, cmd_args):
        """move file or folder"""
        if self.parameter_check(cmd_args, exact_args=2):
            self.send_msg("mv", original_path=cmd_args[0], target_path=cmd_args[1])
            response = self.get_response()
            print(response.get("status_msg"))

    def _rm(self, cmd_args):
        """remove file or folder"""
        if self.parameter_check(cmd_args, exact_args=1):
            self.send_msg("rm", target_path=cmd_args[0])
            response = self.get_response()
            print(response.get("status_msg"))

    def _mkdir(self, cmd_args):
        """make an empty folder"""
        if self.parameter_check(cmd_args, exact_args=1):
            self.send_msg("mkdir", target_path=cmd_args[0])
            response = self.get_response()
            print(response.get("status_msg"))

    def _get(self, cmd_args):
        """download file from ftp server"""
        if self.parameter_check(cmd_args, min_args=1):
            # 1.拿到文件名
            filename = cmd_args[0]
            # 2.发送给服务器
            self.send_msg(action_type="get", filename=filename)
            # 3.等待服务器返回信息
            response = self.get_response()
            # 3.1、如果文件存在，拿到文件大小并写入文件
            if response.get("status_code") == 712:
                recv_size, total_data, file_size = 0, b"", response.get("file_size")
                # 存储下载文件信息，已实现断点续传
                recv_file_info = {
                    "file_name": filename,
                    "file_size": file_size,
                    "file_path": self.current_dir,
                    "file_MD5": response.get("file_md5"),
                    "received": False
                }
                self.rw_file(recv_file_info)
                file_path = "%s\%s.download" % (os.path.dirname(os.path.abspath(__file__)), filename)
                file = open(file_path, "wb")
                progress_bar = tqdm.tqdm(file_size)
                while recv_size < file_size:
                    data = self.sock.recv(file_size - recv_size if file_size - recv_size < 8192 else 8192)
                    progress_bar.set_description("Progressing: %s" % recv_size)
                    recv_size += len(data)
                    total_data += data
                    file.write(data)
                else:
                    file.close()
                    try:
                        os.rename(file_path, "%s" % filename)
                    except FileExistsError:
                        print("Local file already exist!")
                    md5 = hashlib.md5()
                    md5.update(total_data)
                    if md5.hexdigest() != response.get("file_md5"):
                        print("File MD5 value is not match.")
                        os.remove("%s" % filename)
                    else:
                        print("File [%s] received done, received size [%s]".center(50, "-") % (filename, file_size))
                        recv_file_info["received"] = True
                        self.rw_file(recv_file_info)
            else:
                # 3.2、如果文件不存在，打印状态信息
                print(response.get("status_msg"))

    def _put(self, cmd_args):
        """上传本地文件到服务器"""
        if self.parameter_check(cmd_args, exact_args=1):
            local_file = cmd_args[0]
            if os.path.isfile(local_file):
                upload_size, total_size = 0, os.path.getsize(local_file)
                self.send_msg("put", file_size=total_size, file_name=local_file)
                with open(local_file, "rb") as file:
                    progress_bar = tqdm.tqdm(total_size)
                    for line in file:
                        self.sock.send(line)
                        upload_size += len(line)
                        progress_bar.set_description("Progressing: %s" % upload_size)
                    else:
                        print("File upload done.".center(50, "-"))

    def get_response(self):
        """获取服务器返回数据"""
        return json.loads(self.sock.recv(self.MSG_SIZE).decode("utf-8"))

    def send_msg(self, action_type, **kwargs):
        """打包消息内容"""
        msg_data = {
            "action_type": action_type,
            "fill": ""
        }
        msg_data.update(kwargs)
        bytes_msg = json.dumps(msg_data).encode("utf-8")
        if self.MSG_SIZE > len(bytes_msg):
            msg_data["fill"] = msg_data["fill"].zfill(self.MSG_SIZE - len(bytes_msg))
            bytes_msg = json.dumps(msg_data).encode("utf-8")
        self.sock.send(bytes_msg)

    def rw_file(self, data):
        file_item = ""
        result = [data["file_name"], data["file_size"], data["file_path"], data["file_MD5"], data["received"]]
        for item in result:
            file_item += str(item) + ","
        file_item += "\n"
        if data["received"]:
            with open(self.log_path, "r") as file:
                file_list = file.readlines()
            file_list.pop()
            file_list.append(file_item)
            with open(self.log_path, "w") as file:
                for item in file_list:
                    file.write(item)
        else:
            with open(self.log_path, "a") as file:
                file.write(file_item)

    @staticmethod
    def parameter_check(args, min_args=None, max_args=None, exact_args=None):
        """检查参数合法性"""
        if min_args:
            if len(args) < min_args:
                print("Must provide at least %s parameters but %s received." % (min_args, len(args)))
                return False
        if max_args:
            if len(args) > max_args:
                print("Must provide at most %s parameters but %s received." % (max_args, len(args)))
                return False
        if exact_args:
            if len(args) != exact_args:
                print("Must provide exactly %s parameters but %s received." % (exact_args, len(args)))
                return False
        return True


def main():
    client = FtpClient()
    client.interactive()
