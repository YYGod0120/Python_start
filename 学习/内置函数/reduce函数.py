'''
reduce():函数会对参数序列中元素进行累积。函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
语法：
reduce(function函数, iterable[列表])
'''
from functools import reduce
a = [1,1,2,2]
#定义函数
def add(x,y):
    return x * y
print(reduce(add,a))

#通过匿名函数
print(reduce(lambda c,d:c^d,a))
