import time
print(time.time()) #显示时间戳

t = time.localtime()

print(time.localtime()) #将时间戳转化为一个时间对象
#time.struct_time(tm_year=年份, tm_mon=月, tm_mday=日, tm_hour=小时, tm_min=几分, tm_sec=几秒, tm_wday=周几, tm_yday=一年中的第几天, tm_isdst=是否是夏令日)
print(time.gmtime()) #将时间戳转化为零时区的时间对象

print(time.mktime(time.struct_time(time.localtime()))) #将时间对象转化为时间戳

print(time.strftime('%Y-%m-%d %H:%M',t)) #将把⼀个代表时间的元组或者struct_time转化为格式化的时间字符串，若没有不指定t如%xxx，则传入time.localtime

print(time.strptime('2017-10-3 17:54','%Y-%m-%d %H:%M')) #是time.strftime的逆操作


print(time.mktime(time.struct_time(t)))


