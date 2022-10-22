from 包.Stack import Stack
def change(text):
    ans = Stack()
    while text > 0:
        ans.push(text%2) #求余数
        text = text // 2 #求整数
    answer = ''  #准备空字符集接收数据，用来返回二进制数字
    while not ans.isEmpty():
        answer += str(ans.pop()) #利用栈的弹出，从大到小输出
    return int(answer)

print(change(215

             ))