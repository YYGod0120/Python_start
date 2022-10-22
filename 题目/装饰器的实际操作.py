#编写用户登入系统(初级版)
login_check = True
def login_verify(fn):
    def inner(*args,**kwargs):
        global login_check
        if login_check == True:
            while 1:
                admin = input('请输入你的用户名：')
                password = input('请输入你的密码：')
                if admin == 'yeyan' and password == '123456':
                    print('登入成功')
                    login_check = False
                    break
                else:
                    print('登入失败')

        ret = fn(*args, **kwargs)
        return ret
    return inner
@login_verify
def add():
    print('添加员工信息')

@login_verify
def delete():
    print('删除员工信息')

add()
delete()

