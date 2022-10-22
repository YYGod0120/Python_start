#1.字符串的格式化
name = input("请输入你的名字:")
age = int(input("请输入你的年龄:"))
address = input("请输入你的居住地址:")

# %s表示字符串占位
# %d表示整数占位
# %f表示小数占位
s = "我叫%s，我的年龄是%d，我住在%s." % (name,age,address)#小括号一一对应
s0 = "我叫%s" % name
print(s)
print(s0)

#{}占位法
s1 = "我叫{}，我的年龄是{}，我住在{}.".format(name,age,address)#{}加.format
print(s1)

#f-string用法
s2 = f"我叫{name},我的年龄是{age},我住在{address}."
print(s2)



