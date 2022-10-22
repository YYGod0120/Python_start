from 包.Stack import Stack
def parCheck(text):
    s = Stack()
    balance = True
    index = 0
    while index < len(text) and balance:  #遍历案例
        symbol = text[index]
        if symbol == "(":   #扫描到左括号，压入栈
            s.push(symbol)
        else:
            if s.isEmpty():  #扫描到右括号但是栈内为空，匹配失败
                balance = False
            else:
                s.pop()  #栈内删除左括号
        index += 1
    if balance and s.isEmpty():  #扫描结束，栈内为空,匹配成功
        return True
    else:
        return False

print(parCheck('((()))'))

a = '07'
print(int(a))