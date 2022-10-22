ans = 0
def cheng(A,B):
    global ans
    if A == 0:
        return ans
    ans += B
    return cheng(A-1,B)

print(cheng(89,4))

