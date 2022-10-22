#lambda表达式：变量 = lambda 参数一，参数二，参数三..... : 返回值
a_b = lambda a,b : a+b #a_b是个函数，是叫匿名函数，返回值是a+b
print(a_b)
ret = a_b(12,35)
print(ret)