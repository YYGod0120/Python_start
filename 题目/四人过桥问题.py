# 1,2,5,10
# by ma
import random  # 随机从list选出一个，并移除


def ramdon_list(n):
    index = int(random.random() * 10) % (len(n))
    return n.pop(index)


a = [1, 2, 5, 10]
min_time = 100
min_str = ''
for count in range(0, 1000):  # 跑1000次，找出时间最少的组合
    a1 = a[:]  # a的副本
    b = []  # 已经过桥的
    # go
    i = ramdon_list(a1)
    j = ramdon_list(a1)
    b.append(i)
    b.append(j)
    # back
    k = ramdon_list(b)
    a1.append(k)

    # go
    l = ramdon_list(a1)
    m = ramdon_list(a1)
    b.append(l)
    b.append(m)
    # back
    n = ramdon_list(b)
    a1.append(n)

    # go
    o = ramdon_list(a1)
    p = ramdon_list(a1)
    b.append(o)
    b.append(p)

    # print('a',str(a1))
    # print('b',str(b))

    time = max(i, j) + k + max(l, m) + n + max(o, p)  # 过桥时间
    # print('time:',str(time),end='|')
    time_str = ['go', str(i), str(j), 'back', str(k), 'go', str(l), str(m), 'back', str(n), 'go', str(o), str(p)]  # 组合
    # print(' '.join(time_str))

    if min_time > time:  # 筛选最小值
        min_time = time
        min_str = time_str

print('time:', str(min_time), end='|')
print(' '.join(min_str))







