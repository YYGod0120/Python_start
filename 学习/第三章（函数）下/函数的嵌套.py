#函数可以嵌套函数
def a():
    def b():      #局部函数
        print(1)
    b()
    return b #结束进程 返回b函数，不加()


#括号表示运行这个函数，所以函数传递不加括号
#函数也可以作为变量进行返回
c = a  #a指的是a()里面的b函数
c()

#函数可以作为实参进行传递

def c(an):  #an收到了一个函数d
    an()
def d():
    print('我是d')

e = 456
c(d)
#叫做代理模式


