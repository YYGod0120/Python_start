#用find查找
name = '我叫叶焱'
a = name.find('叶焱')
b = name.find('余')
print(a)
print(b)
#返回的数字即为该字符串的位置，若为-1则说明不存在

#index查找
c = name.index("我")
#d = name.index('余')
print(c)
#返回的数字即为位置，报错说明不存在
#print(d)


#in或者not in 查找
print('叶焱' in name)
print('余' in name)
#用in则存在为ture，不存在为false

#startswith用于开头判断，endswith用于结尾判断
d = input('请输入你的名字:')
if d.startswith('叶'):
    print('你姓叶')
else:
    print('你不姓叶')

#isdigit用于整数判断，isdecimal用于小数判断
money = input('请输入你兜里的钱:')
if money.isdigit():
    print('买个东西')
else:
    print('输入错误')

#my_str.count(sub_str[, start[, end]]),
#返回字符串 my_str 中子串 sub_str 出现的次数，可以指定从开始（start）计算到结束（end）。
text = '1223355468777789'
print(text.count('2'))


#str.join(可迭代对象)

