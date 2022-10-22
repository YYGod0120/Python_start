#递归版
def erfen(nums,item):
    first = 0
    last = len(nums)
    mid = (first+last)//2
    if mid > 0:
        if nums[mid] == item:
            return '存在'
        elif nums[mid] > item:  #在右边
            return erfen(nums[:mid],item)
        else:
            return erfen(nums[mid+1:],item)
    else:
        return '不存在'
a = [1,2,3,4,5,6]
print(erfen(a,6))
