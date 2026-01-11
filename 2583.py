from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

n,m,k=map(int,input().split())
mat=[[0 for i in range(m)] for j in range(n)]

for i in range(k):
    x1,y1,x2,y2=map(int,input().split())

    for col in range(x1,x2):
        for row in range(y1,y2):
            mat[n-row-1][col]=1

def sol(u,v,s=None): #dfs로
    moves=[(u+1,v),(u-1,v),(u,v+1),(u,v-1)]
    mat[u][v]=1
    if s is None:
        s=[1]
    for m1,m2 in moves:
        if 0<=m1<n and 0<=m2<m and mat[m1][m2]==0:
            s[0]+=1
            sol(m1,m2,s)
    return s[0]
    
cnt=0
result=[]
for i in range(n):
    for j in range(m):
        if mat[i][j]==0:
            result.append(sol(i,j))
            cnt+=1
print(cnt)
result.sort()
print(*result)