# #能装东西的东西
# #[]来表示列表，用,隔开元素，什么的能添加进列表包括Bool，数字，字符串
a = ['叶焱','abc','123',123]
# print(a)
#
# #特性
#    #1.列表与字符串一样可以索引和切片
# print(a[3])
# print(a[1:3])
# print(a[ : : -1])
# #索引超过范围会报错


#2.用for循环遍历
for item1 in a[1::-1]:#循环列表内元素
    print(item1)
# for index in range(len(a)):#循环列表的索引
#     print(index)

#3.一样可以用len算长度
print(len(a))

b = ['123']
a = [1,2,3,4]
print(sum(a[1:3]))