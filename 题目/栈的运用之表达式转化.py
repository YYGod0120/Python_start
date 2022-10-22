text = ['5','*','6','+','4']
answer = []
text_stock = []
for i in text:
    if i == '(' or i == '*' or i == '/': #(*/ 可以直接压入
        text_stock.append(i)
    elif i in '123456789':
        answer.append(i) #数字直接放到最后答案中
    elif i == ')':
        stockTOP1 = text_stock[-1]  #)需要匹配(，不断弹出栈顶元素直到匹配到元素
        while stockTOP1 != '(':
            answer.append(stockTOP1)
            text_stock.pop()
            stockTOP1 = text_stock[-1]
        text_stock.pop()
    else:  #最后判断+-号，栈顶没有*/则直接压入，有*/则弹出*/然后压入
        stockTOP2 = text_stock[-1]

        if stockTOP2 != '*' and stockTOP2 != '/':
            text_stock.append(i)

        else:

            answer.append(stockTOP2)
            text_stock.pop()
            text_stock.append(i)
for s in text_stock:  #最后遍历栈，弹栈输出答案
    answer.append(s)

print(''.join(answer))








