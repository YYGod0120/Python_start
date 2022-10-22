def F(n):
    for step in range(3,n+1):
        res[step]=res[step-1]+res[step-2]
    return res[n]



