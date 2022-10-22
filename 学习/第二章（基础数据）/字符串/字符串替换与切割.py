#字符串的切割和替换
#strip()用于字符串删去空格
s = "  你好 ， 我叫 周  杰伦  "
s1 = s.strip()
print(s1)
#lstrip()用于字符串删去左边空格或者指定字符

#用于编写用户名和密码时去除前后空格
user_name = input("请输入你的用户名:")
pass_word = input("请输入你的密码:")
if user_name.strip() == "叶焱":
    if pass_word.strip() == "123456":
        print("成功")
    else:
        print("失败")
else:
    print("失败")


#replace(old，new）用于字符串替换
name = "叶焱大帅哥"
name1 = name.replace('叶焱','大帅哥')
print(name1)
#也可以用来删去空格，处理数据
n = 'sjd  jdao  lask'
m = n.replace(" ","")
print(m)


#split(用什么切割)用于字符串的切割
#用什么切割，什么会消失
o = "叶_余_王_林"
o1 = o.split('_')
print(o1)#结果位于列表中
o2 = o.split('_余_')
print(o2)
