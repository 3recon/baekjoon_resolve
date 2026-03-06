n,y=map(int,input().split())

dp=[0]*(y+1)
dp[0]=n
for i in range(1,y+1):
    if i-5>=0:
        dp[i]=max(int(dp[i-5]*1.35),int(dp[i-3]*1.2),int(dp[i-1]*1.05))
        # 5년 적금
    elif i-3>=0:
        # 3년 적금
        dp[i]=max(int(dp[i-3]*1.2),int(dp[i-1]*1.05))
    elif i-1>=0:
        # 1년 적금
        dp[i]=int(dp[i-1]*1.05)
print(dp[-1])