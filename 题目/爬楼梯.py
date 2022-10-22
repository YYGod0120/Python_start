dp = [0] *5000
dp[0] = 1
dp[1] = 2
for i in range(2,len(dp)):
    dp[i] = dp[i-1] + dp[i-2]
def louti(N):
    if N == 1:
        return dp[0]
    elif N == 2:
        return dp[1]
    else:
        return dp[N-1]
print(louti(5000))
