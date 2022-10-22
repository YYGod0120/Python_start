#计算机内最小单位，所以数据均以字节为基本
#计算机存在俩种编码，gbk(16bit,2bytes)和utf-8(英文:8bit,1bytes|中文:24bit,3bytes)

#utf-8和gbk无法直接转化，windows用的是gbk，mac用的是utf-8


s = '周杰伦'
bs = s.encode('gbk') #编码
bs2 = s.encode('utf-8')
print(bs)
print(bs2)
#\xxx为一个bytes
#b\xx\xx叫做bytes类型

#将gbk转化为utf-8类型

a = b'\xd6\xdc\xbd\xdc\xc2\xd7'
b = a.decode('gbk') #解码
c = b.encode('utf-8') #编码
print(c)


d = '我爱abc'
print(d.encode('utf-8'))#utf-8中的英文可以直接表示 b'\xe6\x88\x91\xe7\x88\xb1abc'