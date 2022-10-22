#比较运算符号:= >= <= !=(不等于)

a = 10
b = 40
#如何进行互换
#非python方法:中间值
temp = int()
temp = a
a = b
b = temp
print(a)
print(b)
#python方法
c = 15
d = 35
c,d = d,c
print(c)
print(d)
