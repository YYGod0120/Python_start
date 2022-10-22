import re

a = re.findall('\d+','我的电话是135,你的电话是13596')
print(a)
#找寻整个字符串符合正则的内容，用列表装

b = re.finditer('\d+','我的电话是135,你的电话是13596')
for i in b:
    print(i.group()) #用for循环和.group()取迭代器里的内容
#找寻整个字符串，用迭代器装

c = re.search('\d+','我的电话是135,你的电话是13596')
print(c.group())
print(c.group())
#一找到内容就返回，所以只有一个值

c = re.match('\d+','我的电话是135,你的电话是13596')
#从头开始匹配。
print(c)  #None


#正则表达式预加载
obj = re.compile('\d+')

s = obj.finditer('哦我的名字是006')
for i in s:
    print(i.group())


s1 = """
<div class='jay'><span id='1'>郭麒麟'</span></div>
<div class='jss'><span id='2'>'郭麒'</span></div>
<div class='jy'><span id='3'>'郭麟'</span></div>
<div class='jj'><span id='4'>'麟'</span></div>
"""
#(?P<分组名字>正则),可以单独从正则匹配的内容中提取到xxx东西
obj2 = re.compile("<div class='(?P<na>.*?)'><span id='(?P<id>\d+)'>.*?'</span></div>",re.S) #re.S能让.匹配换行符

result = obj2.finditer(s1)
for it in result:
    print(it.group('na'))
    print(it.group('id'))