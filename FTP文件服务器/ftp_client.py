#!/usr/bin/env python3
# coding = utf-8
#ftp客户端
'''
name:zipeng
email:z.zipeng@qq.cnm
env: python3.5
'''
from socket import *
import sys
from time import sleep

# 具体功能实现


class FtpClient(object):
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L')  # 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
        else:
            # 无法操作
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit('谢谢使用')

    def do_get(self, filename):
        self.sockfd.send(('G '+filename).encode())
        data = self.sockfd.recv(128).decode()

        if data == 'OK':
            fd = open(filename, 'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
            print('%s下载完成' % filename)
        else:
            print(data)

    def do_put(self, filename):
        try:
            fd = open(filename, 'rb')
        except Exception:
            print('文件不存在')
        else:
            while True:
                opinion = input(
                    '%s已读取，输入"yes"确定上传,"no"取消上传' % filename)
                if opinion == 'no':
                    fd.close()
                    return
                elif opinion == 'yes':
                    filename = filename.split('/')[-1]
                    self.sockfd.send(('yes '+filename).encode())
                    data = self.sockfd.recv(128).decode()
                    if data == 'OK':  # 判断服务器是否允许上传
                        while True:
                            data = fd.read(1024)
                            if not data:
                                sleep(0.1)
                                self.sockfd.send(b'**')
                                break
                            sleep(0.1)
                            self.sockfd.send(data)
                        fd.close()
                        data = self.sockfd.recv(128)
                        print(data.decode())
                        break
                    else:
                        print(data)
                else:
                    print('选择错误')


def main():
    if len(sys.argv) < 3:　#判断终端输入是否正确
        print('argv is error')
    HOST = sys.argv[1]　　
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)　#获取终端输入的ip和端口

    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print('链接服务器失败', e)
        return

    # 创建类对象
    ftp = FtpClient(sockfd)
    while True:
        print('\n=======命令选项===========')
        print('***     　list        ***')
        print("***     get file      ***")
        print('***     put file      ***')
        print("***       quit        ***")
        print('=========================')

        cmd = input('输入命令')
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            # 获取文件名
            filename = cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.split(' ')[-1]
            ftp.do_put(filename)
        else:
            print('请输入正确命令')

if __name__ == '__main__':
    main()
