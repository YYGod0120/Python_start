#字典的嵌套
yeyan = {'name':'叶焱','age':18,'wife':{'name':'余文静','age':18}}
print(yeyan['wife']['name'])
yeyan['wife']['age'] = yeyan['wife']['age'] + 1
print(yeyan)


#字典的循环

#1.for循环拿key
dic = {2:12,3:23,4:34,5:45}
for k in dic:
    print(k,dic[k])

#2.将拿到的key放在一个列表中
print(list(dic.keys()))
#3.把所有的value放在一个列表中
print(list(dic.values()))
#4.把所有的key和value放列表中
print(list(dic.items()))

for item in dic.items():
    print(item)

#解构(解包)，元组和列表均可以此操作
a,b = 1,2
c,d =(3,4)
print(a,b)
print(c,d)
#需要一对一，包数不能多

#因为dic.items正好为俩位数，所以将解构用上for循环找key和value
ll = []
for key,value in dic.items():
    ll.append(value)
    ll.append(key)
print(ll)



aaaa = [1,2,3,2]
bbbbb = set(aaaa)
print(len(bbbbb))