text = [1,2,3,4,5,6]
def sum11(text):
    if len(text) == 1:  #基本结束条件
        return text[0]
    else:
        return text[0]+sum11(text[1:]) #调用自身并且减小问题规模

print(sum11([1,2,3,4,5,6]))