#交集用&或者.intersection()
a = {1,2,3}
b = {2,3,4}
print(a & b)
print(a.intersection(b))
#并集用|或者.union()
print(a | b)
print(a.union(b))

#差集用-
print(a - b)
print(b - a)

#删重利器set
lst = [123,123,123,456,456,77,77,895,'叶焱','叶焱']
print(lst)
print(set(lst))#属于set类型
print(list(set(lst)))#属于list类型，但是是无序的
