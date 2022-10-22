#文件修改
import os
import time

with open('../学习/第二章（基础数据）/文件操作/人名单.txt', mode='r', encoding='utf-8') as f:
    with open('../学习/第二章（基础数据）/文件操作/人名单_副本.txt', mode='w', encoding='utf-8') as f2:
        for i in f:
            i = i.strip()#去掉\n,去掉换行
            if i.startswith('张'):
                i = i.replace('张','周')#字符串无法修改，所以需要重新赋值
            f2.write(i)
            f2.write('\n')
#修改文件，将副本保留，源文件删除
#import os代表引入和操作系统相关的模块
time.sleep(3)
os.remove('../学习/第二章（基础数据）/文件操作/人名单.txt')
time.sleep(3)
os.rename('../学习/第二章（基础数据）/文件操作/人名单_副本.txt', '../学习/第二章（基础数据）/文件操作/人名单.txt')
#import time可以用来使程序休眠



