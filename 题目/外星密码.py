import string
ss = input()

def unpack(ss):
    ans = ''
    index1 = 0
    stock_str = []
    a = 0
    while index1 < len(ss):
        if ss[index1] in string.ascii_uppercase:
            stock_str.append(ss[index1])
            index1 += 1
        elif ss[index1] == '[':
            ans.join(stock_str)
            stock_str = []
            index1 += 1
        elif ss[index1] == int:
            a = int(ss[index1])
            index1 += 1
        elif ss[index1] == ']':
            ans.join(stock_str*a)
            index1 += 1
    return ans


print(unpack(ss))