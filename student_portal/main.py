#!/usr/bin/env python3
# coding = utf-8
# 学生信息管理系统的主模块

'''
name:zipeng
email:z.zipeng@qq.cnm


introduce:Student data management
env: python3.5

'''

from student_info import *
from menu import *


def select():
    infos = []  # 此列表用来保存所有学生的信息的字典
    while True:
        show_menu()
        select = input('请选择要使用的功能')
        if select == '1':
            L = input_student()
            infos.extend(L)
            print('\n')
            print('____已添加完成_____')
            sleep_time()

        elif select == '2':
            output_studentn(infos)
            sleep_time()

        elif select == '3':
            del_student(infos)
            sleep_time()

        elif select == '4':
            change(infos)
            sleep_time()

        elif select == '5':
            student_sort(infos)
            sleep_time()

        elif select == '6':
            student_reverse(infos)
            sleep_time()

        elif select == '7':
            student_age(infos)
            sleep_time()

        elif select == '8':
            student_age_reverse(infos)
            sleep_time()

        elif select == '9':
            infos += student_read()
            sleep_time()

        elif select == '10':
            student_write(infos)
            sleep_time()

        elif select == 'q':
            break

        else:
            print('没有这个选项')
            continue


if __name__ == '__main__':
    select()
