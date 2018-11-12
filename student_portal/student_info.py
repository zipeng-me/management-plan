# My_method

from menu import *
from student import Student


def output_studentn(info):
    print('+---------------+-----------+----------+')
    item_name = '|' + '姓名'.center(13) + '|'\
                    + '年龄'.center(9) + '|'\
                    + '成绩'.center(8) + '|'
    print(item_name)
    print('+---------------+-----------+----------+')
    for item in info:
        n, a, s = item.get_infos()
        a = str(a)
        s = str(s)
        get_chinese = chinese_count(n)
        print('|' +
              n.center(15 - get_chinese) +
              '|' +
              a.center(11) + '|' +
              s.center(10) + '|')
    print('+---------------+-----------+----------+')


def chinese_count(x):
    count = 0
    for i in x:
        if ord(i) > 127:
            count += 1
    return count


def student_sort(dicts):
    dic = dicts.copy()
    result = dic.sort(
        key=lambda dic: dic.original_score(), reverse=True)
    output_studentn(dic)


def student_reverse(dicts):
    dic = dicts.copy()
    result = dic.sort(
        key=lambda dic: dic.original_score())
    output_studentn(dic)


def student_age(dicts):
    dic = dicts.copy()
    result = dic.sort(
        key=lambda dic: dic.original_age(), reverse=True)
    output_studentn(dic)


def student_age_reverse(dicts):
    dic = dicts.copy()
    result = dic.sort(
        key=lambda dic: dic.original_age())
    output_studentn(dic)


def change(infos):
    name = input('请输入要修改学生成绩的姓名：')
    L = [n.original_name() for n in infos]
    if name in L:

        score = float(input('请输入修改后的成绩'))
        if score < 0:
            print('不允许成绩为负数')
        else:
            for i in infos:
                if i.original_name() == name:
                    i.get_score(score)
                    print('已修改成绩为:', score)
                    return
    else:
        print('没有这个学生')


def del_student(info):
    name = input('请输入要删除学生的姓名：')
    for i in info:
        if i.original_name() == name:
            info.remove(i)
            print('\n')
            print('已删除:%s' % name)
            return
    print('没有这学生')


def input_student():
    L = []
    while True:
        name = input('请输入姓名　([在这]按回车结束输入)：')
        if not name:
            break
        try:
            age = int(input('请输入年龄：'))
            score = float(input('请输入成绩：'))
            d = Student(name, age, score)
            L.append(d)
        except ValueError:
            print('输入错误，请重新输入')
    return L


def student_write(L, filename='student.txt'):

    if not L:
        print('\n')
        print('请先添加　或　读写文件在保存')
        print('\n')
        print('\n')
        return
    else:
        try:
            file = open(filename, 'w')
            try:
                for d in L:
                    d.get_write(file)
            finally:
                file.close()
        except:
            print('文件写入失败')
    print('文件保存成功')


def student_read(filena='student.txt'):
    L = []
    try:
        file = open(filena)
        while True:
            data = file.readline()
            if not data:
                break
            data = data.strip()
            lis = data.split(',')
            name, age, score = lis
            age = int(age)
            score = float(score)
            L.append(Student(name, age, score))
        print('文件读取完成')
        file.close()
    except OSError:
        print('还没有这个文件')
    return L
