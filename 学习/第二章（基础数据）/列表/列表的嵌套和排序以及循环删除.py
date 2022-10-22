#嵌套[][][]
a = ['叶','余','张',[123,546,789,['yes','no']]]
print(a[3][3][0])
print(a[3][3][0].upper())

#排序用sort，默认升序
b = [12,345,78910,569,1,2]
b.sort()
print(b)
b.sort(reverse=True)#降序
print(b)

#列表的循环删除
#删除大写开头字母的单词
c = ['Python','Java','Wifi','c++']
#print(c[2].capitalize())
#for word in c:
#    if word == word.capitalize():
#        c.remove(word)
#print(c)#出bug会删不干净

#正确方法是做一个新列表把要删除的元素扔进去然后删掉原列表里的新列表元素
d = []
for i in c:
    if i == i.capitalize():
        d.append(i)
print(d)
for rubbish in d:
    c.remove(rubbish)
print(c)



