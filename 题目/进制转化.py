def change(num,base):
    base_code = '0123456789ABCDEF'
    if num<base:
        return base_code[num] #完成条件
    else:
        return change(num//base,base)+base_code[num%base] #调用自身函数简化问题

print(change(54,16))