def func():
    a = 10
    def inner():
        nonlocal a
        print(a)
        a += 1
        return a
    return inner  #形成了一个闭包
#可以使a变量不容易改变的同时可以调用a变量
#闭包本质是内层函数对外层函数的使用，内层函数被称为闭包函数


ret = func()#实质上是func函数是用inner()
print(ret())
