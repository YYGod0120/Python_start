#w模式为写,如果不存在目标文件则会创建新的文件夹，若存在目标文件则会清空文件
f = open('余文静.txt', mode ='w', encoding ='utf-8')
f.write('叶美女')
#写入列表内容:
lst = ['520','1314','584']
#用for循环写
for i in lst:
    f.write(i)
    f.write('\n')
f.close()#最好要加
#close和open大多情况下均写在循环外面

#append模式：a模式，追加写法，不会清空文件
f2 = open('余文静.txt', mode='a', encoding='utf-8')
f2.write('yyy')
f2.close()
