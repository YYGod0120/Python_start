#int属于整数，用于加减乘除
a = 10
print(type(a))
print(a)

#float属于小数，存在误差
b = 10/3
print(type(b))
print(b)

#Bool属于布尔代数，只存在True和False
#所有非零数转化为Bool时均为True，零为False
c = 0
a1 = bool(a)
b1 = bool(b)
c1 = bool(c)
print(a1,b1,c1)

#字符串为空时转化为Bool时属于False
name = "叶焱"
kon = ""
name1 = bool(name)
kon1 = bool(kon)
print(kon1,name1)

#在python中所以表示空的内容在Bool上均为False，相反存在东西表示True
list = []
list2 = [0]
print(bool(list))
print(bool(list2))


#根据这个bool特性，可以方便while循环
while 1:
    content = input("请输入内容:")
    if content == "":
        break
    else:
        print(content)



