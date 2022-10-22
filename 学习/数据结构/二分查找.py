nums = [1,2,5,9,10]
item = 1
first = 0
last = len(nums)

#非递归版
while first <= last:  #循环条件也是终止条件
    mid = (first + last) // 2
    if nums[mid] == item:
        print(f'存在，并且下标为{mid}')
        break
    elif nums[mid] < item:  #说明要查找的内容在中间右边
        first = mid+1
    else:       #说明要查找的内容在中间左边
        last = mid-1
if first > last:
    print('不存在')


