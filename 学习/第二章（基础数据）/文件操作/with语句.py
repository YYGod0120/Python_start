#不用写.close用with语法
with open('叶焱是大帅哥.txt', mode='r', encoding='utf-8') as f:#f = open()
    for line in f:
        print(line.strip())
#已经close了

#用with开非文本文件
#语法:with open('桌面.png',mode = 'rb') as z:#非文本文件在mode后加b，且无encoding=


#复制照片去其他文件夹
with open('桌面.png', mode ='rb') as z:  #rb的意思是用二进制去读代码，同时也有wb，用二进制去写文本:xxx.write(xxx.encode('utf-8'))
    with open('../../桌面2.png', mode ='wb') as z2:
        for line in z:
            z2.write(line)
