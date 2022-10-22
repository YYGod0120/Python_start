import datetime
d = datetime.datetime.now() #返回当前的datetime⽇期
print(d)
# d.timestamp(),d.today(), d.timestamp(),d.today(),d.year,d.timetuple()等⽅法可以调⽤

print(datetime.date.fromtimestamp(322222)) #将一个时间戳转化为datetime日期

#时间运算
print(datetime.datetime.now() + datetime.timedelta(4)) #当前时间 +4天
print( datetime.datetime.now() + datetime.timedelta(hours=4)) #当前时间 +4h

#时间替换
print( d.replace(year=2999,month=11,day=30))
