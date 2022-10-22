#2.索引与切片
#索引:从字符串中选出特定位置的元素
v1 = "我叫叶焱"
print(v1[2])#从0开始数到2
print(v1[-1])#-表示从后往前 '焱'

#切片:从字符串中选出一段元素
v2 = 'abcdefghijkmn'
print(v2[2:5])#一样从0开始
#不包含5，即[start:end]中不存在end
print(v2[-3:-1])#原始的只能从左到右
#print(v2[-1:-3])没结果
print(v2[:5])  #从开头开始计算
print(v2[2:])  #从2到结束
print(v2[:])   #从开头到结束

print(v2[2:8:3]) #[start:end:steep] steep指的是步长 不表示步长即为1
print(v2[-1:-8:-2])#表示从右往左

for i in v2:
    print(i)
