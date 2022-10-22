#zip函数
list1 = ['夜宴','zh','lh']
list2 = ['17','18','19']
list3 = ['a','b','c']
#将三个函数整合到一个函数中
#list0 = []
#for i in range(len(list1)):
#    first = list1[i]
#    second = list2[i]
#    third = list3[i]
#    list0.append((first,second,third))

#print(list0)
list0 = zip(list1,list2,list3)
print(list0) #zip本身是个迭代器
lst = list(list0)
print(lst)
#zip函数就是把多个可迭代内容整合到一个元组中

#locals和globals
#locals放在全局时看的是全局变量，放在局部时看的是局部变量
a = 100
print(locals()) #'a': 100
def fun():
    a = 52
    print(locals())
fun()  #'a': 52

#globals无论在哪里都看的时全局变量，和locals用法一致

#内置函数sorted，用于做排序
#s = sorted(list,key=排序函数，reverse))，sorted函数会把list里每一个item返回给key函数进行规则排序
#列表内为数字时
lst1 = [12,57,212,2,985,88,15461]
s0 = sorted(lst1) #从小到大
s1 = sorted(lst1,reverse=True)  #从大到小
print(s0,s1)

#列表内不为数字时
lst2 = ['叶焱','张华是大哥','余文静','xxxxxxx']
#def func(item):  #item对应的是列表内每一项数据
#    return len(item)
#s3 = sorted(lst2,key=func)
#print(s3)  复杂版排序


#简化排序，加上lambda
s3 = sorted(lst2,key=lambda x:len(x))
print(s3)
#sorted排序最终版：s = sorted(列表,key=lambda x:len(x),reverse)按长度排序

list_text = [
    {'id':1,'name':'yeyan1'},
{'id':2,'name':'yey'},
{'id':3,'name':'yn'},
{'id':4,'name':'yeyanasd'},
]

s4 = sorted(list_text,key=lambda n:len(n['name']))
print(s4)

#filter函数：用于筛选
#语法： 变量= filter(lambda x:筛选内容,list)，将list内每个内容都传递给lambda的x中
m = ['叶13','叶57','张12','张78']
m1 = filter(lambda n:n.startswith('叶'),m)
print(list(m1))

#map用于映射
#语法：变量 = map(lambda x :映射内容，list)
b = [1,3,5,7]
b0 = map(lambda x:x**x,b)
print(list(b0))


num1 = [0,2,0]
nums2 = [3,2]
print(nums2+num1
      )