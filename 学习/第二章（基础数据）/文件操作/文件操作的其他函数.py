#seek可以移动光标
#seek可以读
f = open('人名单.txt','r')
f.seek(2)
print(f.readline())


#seek也可以写
f2 = open('seek函数.txt', 'w',encoding='utf-8' )
f2.write('啦啦啦')
f2.seek(3)
f2.write('你好')

#tell用来返回光标位置

print(f2.tell())

