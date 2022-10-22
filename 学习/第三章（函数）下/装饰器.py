#1.函数可以作为参数传递
#2.函数可以作为返回值进行返回
#3.函数名可以作为变量进行赋值


def wrapper(fn):   #wrapper指的是装饰器，fn指的是被装饰的函数（不要加括号）
            #*指的是接收一切位置参数，**指的是接收一切关键字参数
    def inner(*args,**kwargs):
        print('修饰代码')
             #不加*会导致实参传入变成元组和字典，需要*和**解开
        ret = fn(*args,**kwargs) #调用fn,取得fn中的返回值
        print('修饰代码二')
        return ret  #返回返回值
    return inner  #别加括号，加括号的意思是返回函数结果


@wrapper  #target() =  wrapper(target)
def target(one,two):
    print('目标函数')
    print(one,two)
    return 1



a = target(123,456)
print(a)
#装饰器雏形
#当目标函数内有参数时，装饰器也需要存在参数
#装饰器的返回值需要在装饰器内部加ret

#一个函数能够被多次修饰
def wrapper1(fn):
    def inner(*args, **kwargs):
        print('进入wrapper1')
        ret = fn(*args,**kwargs)
        print('退出wrapper1')
        return ret
    return inner
def wrapper2(fn):
    def inner(*args, **kwargs):
        print('进入wrapper2')
        ret = fn(*args,**kwargs)
        print('退出wrapper2')
        return ret
    return inner

@wrapper1
@wrapper2  #先被2修饰再被1修饰
def target(one):
    print(one)
    return 5

target('target')




