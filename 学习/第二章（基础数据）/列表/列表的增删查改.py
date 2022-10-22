#lst的增加->lst.append
lst = []
lst.append('叶焱')
lst.append('余文静')
print(lst)

#insert插入（位置,内容）
lst.insert(0,'叶')
print(lst)
lst.insert(1,'余')

print(lst)
#extend扩展->将列表合并
lst.extend(['张华','赵总'])
print(lst)

#lst的删除
#pop删除(给出被删除的索引，返回被删除的元素)
ret = lst.pop(3)
print(ret)
print(lst)
#remove删除(给出要删除的元素，不返回被删除元素)
lst.remove('叶焱')
print(lst)
a = [5,6,7]
#lst的修改
lst[3] = a[2]
print(lst)

#lst的查询
print(lst[2])
