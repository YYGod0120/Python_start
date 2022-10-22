import numpy as np
print(np.array([1,2,3]))
print(np.arange(10)) #等差数组
print(np.linspace(1,5,9))
print(np.zeros((3,3)))
b = np.random.random(9).reshape(3,3) #改变样式
a = np.arange(9).reshape(3,3)
print(a)
print(a[0,1],a[1,2]) #获取数据

#运算
print(a+b)
print(a*b)

#线性代数
print(a.T)  #转置
print(a@b)  #相乘
print(np.dot(a,b)) #相乘

#合并
c = np.random.random(10).reshape(2,5)
d = np.arange(10).reshape(2,5)
print(np.vstack(c,d)) #列合并
