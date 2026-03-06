m=int(input())

dp=[1,2,4]
for i in range(m):
    n=int(input())

    for i in range(2,n):
        x=dp[-1]+dp[-2]+dp[-3]
        dp.append(x)
    print(dp[n-1])