#def xxx('xxx')括号里放的是形参
#实际调用的时候括号里放的是实参
#编写一个计算器
def cal(a,opt,b):
    if opt == '+' :
        print(a + b)
    elif opt == '-':
        print(a - b)
    elif opt == '*':
        print(a * b)
    elif opt == '/':
        print(a / b)
    else:
        print('滚')
cal(1 ,'+' ,2)
cal(1 ,'*' ,2)
cal(1 ,']' ,2)