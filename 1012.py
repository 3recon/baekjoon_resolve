def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return 
    if matrix[x][y]==0:
        return 
    matrix[x][y]=0

    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)



t=int(input())

for i in range(t):
    n,m,k=map(int,input().split())
    matrix=[[0 for _ in range(m)] for _ in range(n)] #삭제할 부분

    for j in range(k):
        row ,column=map(int,input().split())
        matrix[row][column]=1 #삭제할 부분

    cnt=0
    for x in range(n):
        for y in range(m):
            if matrix[x][y]==1:
                dfs(x,y)
                cnt+=1
    print(cnt)