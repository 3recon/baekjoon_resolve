n=int(input())

cost = [list(map(int,input().split())) for i in range(n)]

cost=[
    [1,2],
    [3,4]
    ]

for i in range(1,n):
    for j in range(3):
        temp=cost[i-1].copy()
        del temp[j]
        cost[i][j]+=min(temp)
print(min(cost[-1]))
