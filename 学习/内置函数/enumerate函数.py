'''
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据下标和数据，一般用在 for 循环当中。
语法：
enumerate(sequence, [start=0])
'''
dic = [1,2,3,5]
for k,v in enumerate(dic):
    print(k,v)


for i in dic:

    dic.remove(i)

print(dic)