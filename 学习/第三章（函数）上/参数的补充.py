lst = ['夜宴','hhh','lalal','一二']
def a(*args):
    print(args)

a(*lst)#*能够将列表里的内容全部打散为位置参数传递给a函数
#**能够将字典里的内容打散为关键字餐参数传递