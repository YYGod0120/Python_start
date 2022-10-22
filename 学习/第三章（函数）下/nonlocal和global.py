#global用于在定义函数外引入数据
a = 10
def an():
    global a  #引入a
    a = 20
an()#运行一下函数a
print(a)

#nonlocal用于局部的局部中引入局部数据

def bn():
    c = 10
    print(c)
    def cn():
        nonlocal c
        c = 20
    cn()
    print(c)

bn()