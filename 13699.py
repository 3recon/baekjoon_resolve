dp=[1,1]
n=int(input())

while len(dp)-1<n:
    result=0
    if len(dp)%2==0:
        for i in range(len(dp)//2):
            result+=(dp[i]*dp[len(dp)-i-1])
        result*=2
    else:
        for i in range(len(dp)//2):
            result+=(dp[i]*dp[len(dp)-i-1])
        result*=2
        result+=dp[len(dp)//2]**2
    dp.append(result)
print(dp[-1])