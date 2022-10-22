#默认参数
def a(yi,er,san='1'):
    print(yi,er,san)
a('456','568')
a('yiyiyi','sadaw','5454')#默认参数可以被覆盖

#动态参数一:*args,收纳一切位置参数
def b(*e):
    print(e)
b(123,121212,'yeyan')
b('yeyan','余文静')
b()
#统一放在元组里

#动态参数二:**kargs,接收一切关键字参数
def c(**c):
    print(c)
c(a='11',name='yeyan',age=16)
#统一放在字典里

#混合使用是的顺序:位置>*args>默认值>**kargs
