#用于简化代码
#列表推导式：lst = [数据 for循环 if判断]
#例子：买50件衣服
lst1 = [f'衣服{i}' for i in range(50)]
print(lst1)
#在一个列表中放下1到100的奇数
lst2 = [i for i in range(100) if i%2 == 1]
print(lst2)

#集合推导式  set = （数据 for循环 if判断）

#字典推导式  dic = {k:v for if}
#把一个列表里的内容扔到字典里，索引当key，内容当value
list_text = ['111','222','333']
dic = {i:list_text[i] for i in range(len(list_text))}
print(dic)

#生成器推导式：gen = (数据,for,if)
gen = (i*3 for i in range(100))
print(gen)
print(gen.__next__())
#获得gen里全部内容
for a in gen:
    print(a)

lst = list(gen)  #list(可迭代) => for => 可迭代
print(lst)