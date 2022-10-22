#实参的分类:实际在调用的时候传递的信息
#1.通过位置进行传递参数
def a(yi,er,san):
    print(yi,er,san)
#一一对应
a('e','a','s')

#2.通过关键字进行传递参数
def b(yi,er,san):
    print(yi,er,san)
b(yi='1',er='2',san='3')

#3.混合参数（必须位置参数在前，关键字参数在后）
def c(yi,er,san):
    print(yi, er, san)
c('1','2',san='3')

#写了几个形参，实参必须写几个，不然报错
