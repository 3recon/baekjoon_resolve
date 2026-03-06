t=int(input())

dp=[1,3]

for i in range(2,t):
    x=dp[-1]+(dp[-2]*2)
    dp.append(x)
print(dp[t-1]%10007)