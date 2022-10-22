#字典的增加xxx.[key] = value
dic = dict()
dic['叶焱'] = '余文静'
dic[1] = 123
print(dic)

dic[1] = 23 #因为dic中存在了1:123,所以现在进行的是修改的步骤
print(dic)
dic.setdefault(4,456)#xxx.setdefault是叫设置默认值，无法进行修改内容
dic.setdefault(4,45)#无效
print(dic)

#删除通过.pop删
dic.pop(1)
print(dic)
#或者用del也可以
#del dic ['叶焱']   #不常用
#print(dic)


#查询,查询的是key而非value
print(dic[4])
print(dic.get(4))
#print(dic[45])#一旦key不存在将报错
print(dic.get(456))#key不存在时会返回None

names = {'张华':'脚臭','叶焱':'大帅哥','余文静':'大美女'}
name = names.get(input('请输入你要查询的人:'))
if name == None :
    print('你所查询的人不存在')
else:
    print(name)
