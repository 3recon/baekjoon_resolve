n=int(input())
step=[int(input()) for i in range(n)]

if n<=2: 
    print(sum(step))
else:
    dp=[0]*n
    dp[0],dp[1]=step[0],step[1]+step[0]
    for i in range(2,n):
        dp[i]=max(step[i] + step[i-1] + dp[i-3], step[i] + dp[i-2])
    print(dp[-1])