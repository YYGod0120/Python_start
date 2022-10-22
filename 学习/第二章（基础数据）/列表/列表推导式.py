'''
其语法格式如下所示，其中 [if 条件表达式] 可省略。

[表达式 for 迭代变量 in 可迭代对象 [if 条件表达式]]
'''
text = [1,2,3,4,5]
text_0 = []
for i in text:
    text_0.append(i*2)
print(text_0)

text_1 = [i*2 for i in text]
print(text_1)
