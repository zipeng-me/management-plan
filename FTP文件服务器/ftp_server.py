
#!/usr/bin/env python3
# coding = utf-8
#ftp服务器
'''
name:zipeng
email:z.zipeng@qq.cnm
env: python3.5
'''
from socket import *
import os
import sys
from threading import Thread
import time

# 全局变量
HOST = '0.0.0.0'
PORT = 8889
ADDR = (HOST, PORT)

FILE_DIR = 'FTP/' #文件库目录


def zombie():
    os.wait()


class FtpServer(object):
    def __init__(self, connfd):
        self.connfd = connfd

    def do_list(self):
        # 获取文件列表
        file_list = os.listdir(FILE_DIR)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        files = ''
        for file in file_list:
            if file[0] != '.' and \
            os.path.isfile(FILE_DIR + file):
                files = files + file + '#'
        self.connfd.send(files.encode())

    def do_git(self, filename):
        try:
            fd = open(FILE_DIR + filename, 'rb')
        except:
            self.connfd.send('文件不存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        # 发送文件内容
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        fd.close()

    def do_put(self, filename):
        self.connfd.send(b'OK')
        try:
            fd = open(FILE_DIR+filename, 'wb')
        except Exception as e:
            self.connfd.send('文件上传失败'.encode())
        else:
            while True:
                data = self.connfd.recv(1024)
                if data == b'**':
                    break
                fd.write(data)
            fd.close()
            self.connfd.send('文件上传成功'.encode())


# 创建网络链接
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(4)

    print('Listen to the port 8888...')

    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器推出")
        except Exception as e:
            print('服务器异常', e)
            continue
        print('链接用户：', addr)

        # 创建子进程
        pid = os.fork()
        if pid == 0:
            sockfd.close()
            ftp = FtpServer(connfd)
            # 循环接受客户端请求
            while True:
                data = connfd.recv(1024).decode()
                if not data or data[0] == 'Q':
                    connfd.close()
                    sys.exit("客户端退出")
                elif data[0] == 'L':
                    ftp.do_list()
                elif data[0] == 'G':
                    filename = data.split(' ')[-1]
                    ftp.do_git(filename)
                elif data[:3] == 'yes':
                    filename = data.split(' ')[-1]
                    ftp.do_put(filename)

            os._exit(0)
        else:
            connfd.close()
            # 单独创建线程处理僵尸进程
            t = Thread(target=zombie)
            t.setDaemon(True)
            t.start()
            continue

if __name__ == '__main__':
    main()
