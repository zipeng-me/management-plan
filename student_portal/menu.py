# menu.py

import time


def show_menu():
    print('\n')
    print('+--------------------------------+')
    print('|1) 添加学生信息                 |')
    print('|2) 查看学生信息                 |')
    print('|3) 删除学生信息                 |')
    print('|4) 修改学生成绩                 |')
    print('|5) 按学生成绩高-低显示学生信息  |')
    print('|6) 按学生成绩低-高显示学生信息  |')
    print('|7) 按学生年龄高-低显示学生信息  |')
    print('|8) 按学生年龄低-高显示学生信息  |')
    print('|9) 从文件中读取数据(student.txt)|')
    print('|10) 保存信息到文件(student.txt) |')
    print('|q) 退出　　　　　               |')
    print('+--------------------------------+')
    print('\n')


def sleep_time():
    print('程序将在　３　秒后自动返回主菜单', end='\r')
    time.sleep(1)
    print('程序将在　２　秒后自动返回主菜单', end='\r')
    time.sleep(1)
    print('程序将在　１　秒后自动返回主菜单', end='\r')
    time.sleep(1)
