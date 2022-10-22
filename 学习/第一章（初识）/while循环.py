#1-2+3-4+5-6.....-100
i = 1
m = 0
t = 0
while i <= 100:
    if t < 1:
        t = t + 1
        m = m + i
    else:
        t = t - 1
        m = m - i
    i = i + 1
print(m)





