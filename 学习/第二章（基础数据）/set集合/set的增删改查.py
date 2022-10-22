#set使用大括号
s = {13,45,'叶焱'}
#a = {13,45,[]}会报错，因为set里只能存放可哈希（hashable）内容
#unhashable:可变的数据类型_list，set，dict
#hashable:不可变的数据类型_int，tuple，str，bool
print(type(s))

#set的空集合为set(),同理空列表，空元组，空字符串均为xx()
k = set()

#增加用add
k.add(123)
k.add('叶焱')
k.add(True)
print(k)

#删除用remove，pop需要索引，set不存在索引
k.remove(True)
print(k)

#查看用for循环
for item in k:
    print(item)
