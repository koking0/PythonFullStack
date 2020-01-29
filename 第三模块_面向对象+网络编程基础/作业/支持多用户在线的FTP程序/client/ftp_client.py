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
import shelve
import socket
import optparse


class FtpClient:
    """Ftp客户端"""

    MSG_SIZE = 1024
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self.username = None
        self.current_dir = None
        self.terminal_display = None
        self.shelve_obj = shelve.open(".ftp_transmit")

        # 处理参数
        parser = optparse.OptionParser()
        parser.add_option("-s", "--server", dest="server", help="ftp server ip address")
        parser.add_option("-P", "--port", type="int", dest="port", help="ftp server port")
        parser.add_option("-u", "--username", dest="username", help="username info")
        parser.add_option("-p", "--Password", dest="password", help="password info")
        self.options, self.args = parser.parse_args()
        self.argv_verification()

        # 建立链接
        self.sock = None
        self.make_connection()

    def _cd(self, cmd_args):
        """change to target dir"""
        if self.parameter_check(cmd_args, exact_args=1):
            target_dir = cmd_args[0]
            self.send_msg("cd", target_dir=target_dir)
            response = self.get_response()

            if response.get("status_code") == 400:
                self.current_dir = response.get("current_dir")
                self.terminal_display = "[%s%s]>>> " % (self.username, self.current_dir)

    def _ls(self, cmd_args):
        self.send_msg(action_type="ls")
        response = self.get_response()

        if response.get("status_code") == 302:
            cmd_result = b""
            cmd_received_size = 0
            cmd_result_size = response.get("cmd_result_size")
            while cmd_received_size < cmd_result_size:
                if cmd_result_size - cmd_received_size < 8192:
                    data = self.sock.recv(cmd_result_size - cmd_received_size)
                else:
                    data = self.sock.recv(8192)
                cmd_received_size += len(data)
                cmd_result += data
            else:
                print(cmd_result.decode("gbk"))

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
            if response.get("status_code") == 300:
                received_size = 0
                file_size = response.get("file_size")

                # save file to shelve db
                file_abs_path = os.path.join(self.current_dir, filename)
                self.shelve_obj[file_abs_path] = [file_size, "%s\%s.download" % (self.CURRENT_DIR, filename)]

                # progress_generator = self.progress_bar(file_size)
                # progress_generator.__next__()

                with open("%s\%s.download" % (self.CURRENT_DIR, filename), "wb") as file:
                    progress_bar = tqdm.tqdm(file_size)
                    while received_size < file_size:
                        data = self.sock.recv(file_size - received_size) if file_size - received_size < 8192 else self.sock.recv(8192)
                        progress_bar.set_description("Progressing: %s" % received_size)
                        received_size += len(data)
                        file.write(data)
                    else:
                        file.close()
                        del self.shelve_obj[file_abs_path]
                        os.rename("%s.download" % filename, "%s" % filename)
                        print("File [%s] received done, received size [%s]".center(50, "-") % (filename, file_size))

            # 3.2、如果文件不存在，打印状态信息
            else:
                print(response.get("status_msg"))

    def _put(self, cmd_args):
        """上传本地文件到服务器"""
        if self.parameter_check(cmd_args, exact_args=1):
            local_file = cmd_args[0]
            if os.path.isfile(local_file):
                upload_size = 0
                total_size = os.path.getsize(local_file)
                self.send_msg("put", file_size=total_size, file_name=local_file)
                with open(local_file, "rb") as file:
                    progress_bar = tqdm.tqdm(total_size)
                    for line in file:
                        self.sock.send(line)
                        upload_size += len(line)
                        progress_bar.set_description("Progressing: %s" % upload_size)
                    else:
                        print()
                        print("File upload done.".center(50, "-"))

    def _auth(self):
        """用户认证"""
        count = 0
        while count < 3:
            count += 1
            # username = input("Please input username: ").strip()
            username = "Alex"
            if not username:
                continue
            # password = input("Please input password: ").strip()
            password = "20001001"
            if not password:
                continue

            self.send_msg(action_type="auth", username=username, password=password)
            response = self.get_response()
            # print("response: ", response)

            if response.get("status_code") == 200:
                self.current_dir = "/"
                self.username = username
                self.terminal_display = "[%s]>>> " % self.username
                return True
            else:
                print(response.get("status_msg"))

    def interactive(self):
        """处理与FtpServer的所有交互"""
        if self._auth():
            self.unfinished_file_check()

            while True:
                user_input = input(self.terminal_display).strip()
                if not user_input:
                    continue
                cmd_list = user_input.split()
                if hasattr(self, "_%s" % (cmd_list[0])):
                    func = getattr(self, "_%s" % (cmd_list[0]))
                    func(cmd_list[1:])

    def argv_verification(self):
        """检查参数合法性"""
        if not self.options.server or not self.options.port:
            exit("Error: must supply server and port parameters")

    def make_connection(self):
        """建立socket链接"""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.options.server, self.options.port))

    def get_response(self):
        """获取服务器返回数据"""
        data = self.sock.recv(self.MSG_SIZE)
        return json.loads(data.decode("utf-8"))

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

    def unfinished_file_check(self):
        """检查shelve db，把没正常接收完的文件列表打印，按用户的指令决定是否重传"""
        if list(self.shelve_obj.keys()):
            print("Unfinished file list".center(50, "-"))
            for index, abs_file in enumerate(self.shelve_obj.keys()):
                received_file_size = os.path.getsize(self.shelve_obj[abs_file][1])
                print("%s. %s    %s    %s    %s" % (index, abs_file, self.shelve_obj[abs_file][0], received_file_size, int(received_file_size / self.shelve_obj[abs_file][0]) * 100))

            while True:
                choice = input("Selected file index to re-download(q to quit): ").strip()
                if not choice:
                    continue
                if "q" in choice or "quit" in choice:
                    break
                if choice.isdigit():
                    choice = int(choice)
                    if 0 <= choice < len(self.shelve_obj.keys()):
                        selected_file = list(self.shelve_obj.keys())[choice]
                        already_received_size = os.path.getsize(self.shelve_obj[selected_file][1])
                        print("Server resend file: ", selected_file)

                        self.send_msg("re_get", file_size=self.shelve_obj[selected_file][0],
                                      received_size=already_received_size,
                                      abs_filename=selected_file)

                        response = self.get_response()
                        if response.get("status_code") == 500:
                            received_size = already_received_size
                            total_size = self.shelve_obj[selected_file][0]
                            local_filename = self.shelve_obj[selected_file][1]
                            with open(local_filename, "ab") as file:
                                progress_bar = tqdm.tqdm(total_size)
                                while received_size < total_size:
                                    data = self.sock.recv(
                                        total_size - received_size) if total_size - received_size < 8192 else self.sock.recv(8192)
                                    progress_bar.set_description("Progressing: %s" % received_size)
                                    received_size += len(data)
                                    file.write(data)
                                else:
                                    del self.shelve_obj[local_filename]
                                    print("File [%s] received done, received size [%s]".center(50, "-") % (local_filename, total_size))
                        else:
                            print(response.get("status_msg"))
                    else:
                        print("Selected number out of index.")


if __name__ == '__main__':
    client = FtpClient()
    client.interactive()
