# 公   司：峦锘科技
# 作   者：潘浩
# 创建时间：2022/3/9 17:28
# 备   注：学生管理简单系统
studentsFileName = 'studentsFile.txt'
def main():
    while True:
        menum()
        choice = int(input('请选择：'))
        if choice in range(0,8):
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢使用')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                find()
            elif choice == 3:
                del_s()
            elif choice == 4:
                edit()
            elif choice == 5:
                sort()
            elif choice == 6:
                stat()
            elif choice == 7:
                show()
        else:
            print('请输入正确选项')
def menum():
    print('==========================学生管理系统============================')
    print('--------------------------菜单选择------------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生数量')
    print('\t\t\t\t\t\t7.显示学生信息')
    print('\t\t\t\t\t\t0.退出系统')
    print('---------------------------------------------------------------')
def insert():
    students = []
    while True:
        id = input('请输入学生id')
        if not id:
            break
        name = input('请输入姓名')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩'))
            java = int(input('请输入java成绩'))
            python = int(input('请输入python成绩'))
        except:
            print('请输入整数成绩')
            continue
        student = {'id':id, 'name':name, 'english':english, 'java':java, 'python':python}
        students.append(student)
        choice = input('是否继续添加学生信息y/n:')
        if choice == 'y' or choice == 'Y':
            continue
        else:
            break

    save(students)
def save(lst, type = 'a'):
    try:
        stu_txt = open(studentsFileName, type, encoding='utf8')
    except:
        stu_txt = open(studentsFileName, 'w', encoding='utf8')
    for item in lst:
        stu_txt.write(str(item)+'\n' if type == 'a' else str(item))
    stu_txt.close()
    show()
def find():
    id = input('请输入要查找学生的ID（10012）：')
    if not id:
        print('id输入错误')
    else:
        stu_txt = open(studentsFileName, 'r', encoding='utf8')
        students = stu_txt.readlines()
        students_edit = []
        for student in students:
            student_info = eval(student)
            if student_info['id'] == id:
                students_edit.append(student_info)
                printT(students_edit)
                break
        stu_txt.close()
def del_s():
    id = input('请输入要删除学生的ID（10012）：')
    if not id:
        print('id输入错误')
    else:
        stu_txt = open(studentsFileName, 'r', encoding='utf8')
        students = stu_txt.readlines()
        for student in students:
            student_info = eval(student)
            if student_info['id'] == id:
                students.remove(student)
                break
        stu_txt.close()
        save(students,'w')
def edit():
    id = input('请输入要修改学生的ID（10012）：')
    if not id:
        print('id输入错误')
    else:
        stu_txt = open(studentsFileName, 'r', encoding='utf8')
        students = stu_txt.readlines()
        i = 0
        for student in students:
            student_info = eval(student)
            if student_info['id'] == id:
                student_info['id'] = input('请输入新ID：')
                student_info['name'] = input('请输入新姓名')
                student_info['english'] = input('请输入english成绩')
                student_info['java'] = input('请输入java成绩')
                student_info['python'] = input('请输入python成绩')
                students[i] = str(student_info)+'\n'
                break
            i+=1
        stu_txt.close()
        save(students, 'w')
def sort():
    while True:
        choice = int(input('请选择排序字段(3.英语成绩排序 4.java成绩排序 5.python成绩排序 6.总分排序 7.退出排序)'))
        if choice in range(3,8):
            if choice == 7:
                break
            else:
                reverse = input('正序/倒序？y/n：') == 'y'
                stu_txt = open(studentsFileName, 'r', encoding='utf8')
                students = []
                for student in stu_txt.readlines():
                    students.append(dict(eval(student)))
                stu_txt.close()
                if choice == 3:
                    students.sort(key=lambda x: int(x['english']),reverse=reverse)
                elif choice == 4:
                    students.sort(key=lambda x: int(x['java']), reverse=reverse)
                elif choice == 5:
                    students.sort(key=lambda x: int(x['python']), reverse=reverse)
                elif choice == 6:
                    students.sort(key=lambda x: int(x['java'])+int(x['python'])+int(x['english']), reverse=reverse)
                printT(students)

def stat():
    stu_txt = open(studentsFileName, 'r', encoding='utf8')
    print('总人数为:', len(stu_txt.readlines()))
    stu_txt.close()
def show():
    stu_txt = open(studentsFileName, 'r', encoding='utf8')
    students = []
    for student in stu_txt.readlines():
        students.append(eval(student))
    printT(students)
    stu_txt.close()
def printT(lst=[]):
    print('\t\t\tID\t\t\t\t姓名\t\t\t\t英语成绩\t\t\t\tjava成绩\t\t\t\tpython成绩\t\t\t\t总成绩')
    for student_info in lst:
        print('\t\t\t{0}\t\t\t{1}\t\t\t\t{2}\t\t\t\t\t{3}\t\t\t\t\t{4}\t\t\t\t\t\t{5}'.format(student_info['id'],student_info['name'],student_info['english'],student_info['java'],student_info['python'],student_info['english']+student_info['jav'
                                                                                                                                                                                                                                               'a']+student_info['python']))

if __name__ == '__main__':
    main()