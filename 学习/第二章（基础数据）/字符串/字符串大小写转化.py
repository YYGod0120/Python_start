#字符串的基本操作
#字符串的操作不会影响到原字符串

s = "python"
s1 = s.capitalize()#使首字母变大写
print(s1)

c = "i have a dream"
c1 = c.title()#使每个单词首字母大写
print(c1)

b = "I HAVE A DREAM"
b1 = b.lower()#使字符串变小写
print(b1)

c2 = c.upper()#使字符串变大写
print(c2)

#验证码输入忽略大小写 => 全部变成大写
verify_code = 'sDI4'
user_code = input(f"请输入验证码({verify_code}):")
if user_code.upper() == verify_code.upper():
    print("成功")
else:
    print("错误")





