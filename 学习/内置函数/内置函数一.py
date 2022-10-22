#转化进制的函数:bin,oct,hex
a = 18 #十进制
print(bin(a)) #0b10010,2进制
print(oct(a)) #0o22,8进制
print(hex(a)) #0x12,16进制

#int除了转化为整数，还可以转化为10进制
print(int(0b10010))

#pow,sum ,max,min
lst = [12,23,56,78,5,111]
b = 2
print(pow(a,b))#a的b次方
print(sum(lst))
print(max(lst))
print(min(lst))


#list函数
s = {1,2,3}
print(list(s))#list的运行逻辑是将s中的元素遍历后再加入到一个列表中,如下面这个代码
kon = []
for i in s:
    kon.append(i)
print(kon)
#slice == 切片


#format ord chr
c = '中'
print(format(a,'08b'))#2进制
#10010只有5个bytes，可以在b前加08变成8bytes的结构，08意思是通过加0补充到8bytes，当超过8字节是不会在添加0

print(format(a ,'o'))#8进制
print(format(a ,'x'))#16进制
print(ord(c))  #通过ord能够将字符变成Unicode中的码位
print(chr(20013))


#all，any ，enumerate
print(all(['0', 12 ,'yey']))  #将all当作and来看
print(any(['0', 12 ,'yey']))  #将any当作or来看

aa = ['yeyan',123,456,'wuwu']
for index,item in enumerate(aa):
    print(index,item)#用于快速将列表中索引和元素列出

s = '呵呵哒'
print(hash(s))  #通过计算算出一个数字，转化成内存位置进行数据存储，字典(列表)的存储
print(id(s))  #直接写出s的内存位置

#help->看源码，在pycharm中直接ctrl加右键看就可以了

#dir能告诉你xxx的操作
print(dir(str))

a = 'yyyy  '
