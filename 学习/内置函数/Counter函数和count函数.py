'''
xxx = Counter()也可以用于统计字符出现的个数或列表中元素出现的次数。返回结果按出现次数从多至少排列。
一个Counter是一个dict的子类，用于计数可哈希对象。
count()函数用来统计一个字符串或列表里某一元素出现的频率



'''
from collections import Counter
ls = [1,1,1,2,3,3,5,5]
cns = Counter(ls)
print(cns)
word = 'aabbc'
for i in range(len(word)):
            cnt = Counter(word[:i] + word[i + 1:]) #删除一个字符
            print(cnt)
            same = cnt.popitem()[1]  #将cnt最末尾的一个字符频率以元组弹出
            print(same)
            if all(c == same for c in cnt.values()):
               print('1')

print(ls.count(1))



