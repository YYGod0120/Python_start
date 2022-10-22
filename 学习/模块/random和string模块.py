'''
一些模块库
random
string
'''
import random
a = random.randint(0, 50)
print(a)
lst = ['1','2','3','4','5']
#随机从0到50中返回一个数，包括0和50

b = random.choice('sadw')
c = random.choice(lst)
#返回一个列表元素或一个字符串的字符

print(b)
print(c)
d = random.sample(lst,4)

d = ''.join(d)
print(d)




import string
#直接导入各种字符
lst2=[string.ascii_letters]
print(lst2)
lst3=[string.ascii_uppercase]
print(lst3)
lst4=[string.digits]
print(lst4)
print(random.__file__)