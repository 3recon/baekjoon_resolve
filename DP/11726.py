n=int(input())

dp=[0]*n
dp[0],dp[1]=1,2
if n<=2:
    print(dp[-1]%10007)
else:
    for i in range(2,n):
        dp[i]=dp[i-1]+dp[i-2]
    print(dp[-1]%10007)

1,2,3,5,8,13