#作用域:指的是变量的访问权限

a = 10 #全局变量，任何地方都能访问
print(a)
def func():
    b = 20  #b是局域变量，无法用于函数外面
    print(b)
    return b  #需要用到定义函数里的b时需要return
#print(b)
func()
b1 = func()
print(b1)

def func3():
    def func2():  #局部函数无法作用于全局
        print(a)
#func2()报错

