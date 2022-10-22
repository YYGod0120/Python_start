#1.找到文件，双击打开，用到open函数,open(文件路径,mode = '',encoding='')
#2.打开文件需要路径:绝对路径：d:/xxx/xxx(少用)  相对路径:如果在本目录下，直接open('文件名')，在外面路径则open(../xxx/xxxx/xxx)
f = open('叶焱是大帅哥.txt', mode='r', encoding='utf-8')  #r指的是read
#passenge = f.read() #全部读取
#line = f.readline()  #读一行（***）(存在\n即换行符)
#lines = f.readlines()   #读每一行且放在列表里

#读取将会把文本内容移走导致后来的read无效

#print(passenge)
#print(line)
#print(lines)
#循环读法:读取每一行信息（存在\n即换行符）用.strip去除
for li in f:
    print(li.strip())