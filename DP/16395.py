n,m=map(int,input().split())

lst=[[0]*(n+1) for i in range(n+1)]

lst[1][1]=1

for i in range(2,n+1):
    for j in range(1,m+1):
        lst[i][j]=lst[i-1][j]+lst[i-1][j-1]
print(lst[n][m])