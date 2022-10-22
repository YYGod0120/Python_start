#可迭代：str，list，tuple，dict，set和open()
#这些东西内部都存在一个迭代器，for循环的原理就是这些迭代器
#通过iter()内置函数和xxx.__iter__()来获取迭代器
a = '呵呵哒'
b1 = iter(a)
b2 = a.__iter__()
print(b1,b2)

#通过next()和xxx.__next__()来获取迭代器里的东西

print(next(b1))
print(b1.__next__())
print(b1.__next__())
#print(b1.__next__())  #StopIteration是因为迭代器里的东西被获取完了无法在获取东西

#for循环遍历原理就是靠迭代器
c = '呵呵哒'
#取迭代器必须在外面取，不然会出bug
c1 = iter(c)
while 1:
    try:  #try是尝试运行不报错则运行
        data = next(c1)
        print(data)
    except:  #报错类型后运行
        StopIteration
        break
#for循环的原理

#迭代器就是方便不同数据的遍历工作
#特性：1.迭代器本身可以迭代
m = '123'
n = iter(m)

for i in n:
    print(i)

#2.迭代器只能向前获取不能反复或者后退
#3.迭代器特别节省内存
#4.迭代器有惰性机制(不使用就不往前走)


