import random
import string
#定义一个函数用来表示随机车牌
def fp():
    global lp_list
    lp_list = []#设置空列表收车牌
    for i in range(0,20):
        word = random.sample(string.ascii_uppercase, 3) #随机数
        number = random.sample(string.digits, 3)  #随机字母
        lp = ''.join(word) + ''.join(number)
        lp_list.append(lp) #扔车牌


fp()
#车牌表示
i0 = 1
for n in lp_list:
    print(f"第{i0}个:", end='')
    print(n, end=' ')
    i0 += 1


#主程序


m = 1
def fina():
    global m #m设为全局变量以便使用

    if m < 3: #限制次数
        want1 = input('你想要的车牌号序号，如果全部不想要，按t换选（你只有三次换选机会）:').strip()
        #换选程序
        if want1 == 't':

            m += 1
            fp()  #套用函数
            i0 = 1
            for n in lp_list:
                print(f"第{i0}个:", end='')
                print(n, end=' ')
                i0 += 1
            fina()
        else:
            print(f'已选中你的{lp_list[int(want1)]}车牌')



    else:
        want2 = input('你想要的车牌号序号(无法再换选):')

        print(f'已选中你的{lp_list[int(want2)]}车牌')



fina()











