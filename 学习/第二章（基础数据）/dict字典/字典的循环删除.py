#字典的删除与列表相同，必须设置空列表放待删除内容
dic = {'叶焱':'帅哥','余文静':'美女','叶哥':'不认识'}
temp = []
for t in dic:
    if t.startswith('叶'):
        temp.append(t)
print(temp)
for r in temp:
    dic.pop(r)
print(dic)