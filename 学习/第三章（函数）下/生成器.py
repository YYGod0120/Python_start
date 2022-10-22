#生成器就是迭代器
#出现yield的时候就说明是生成器函数，生成器函数执行时不会执行函数，
#yield能够使函数一段一段执行
def func():
    print(123)
    yield 999  #yield也有返回的意思
ret = func()
print(ret)  #<generator object func at 0x000002D20772C890>,说明返回了一个迭代器

#ret.__next__()  #999被返回了没人接
#加个print才可以
print(ret.__next__())

#生成器的实例：
#发送10000件衣服，没法一次性接收，所以利用生成器50件50件接收
#lst = []会报错  local variable 'lst' referenced before assignment

def shop():
    lst = []
    for i in range(10000):
        lst.append(f'衣服{i}')
        if len(lst) == 50:
            yield lst
            lst = []  #让列表重新变空 重新接收

gen = shop()
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())







