n=int(input())
wine=[]
for i in range(n):
    x=int(input())
    wine.append(x)

dp=[0]*n
dp[0]=wine[0]

if n<=2:
    print(sum(wine))

else:
    for i in range(1,n):
        dp[i]=max(dp[i-1], dp[i-2] + wine[i], wine[i] + wine[i-1] + dp[i-3])
    print(max(dp))