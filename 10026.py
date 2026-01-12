import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import deque



x=int(input())
mat=[[] for i in range(x)]


for i in range(x):
    color=input().strip()
    for j in color:
        mat[i].append(j)

visited=[[0]*x for i in range(x)]

def sol(r,c,rgb):
    moves=((r+1,c),(r-1,c),(r,c+1),(r,c-1))
    if mat[r][c]=='R' or mat[r][c]=='G' or mat[r][c]=='RG': #0
        visited[r][c]='RG'
    else:
        visited[r][c]='B'
    for r,c in moves:
        if 0<=r<x and 0<=c<x and visited[r][c]==0 and mat[r][c]==rgb: #0
            if mat[r][c]=='R' or mat[r][c]=='G' or mat[r][c]=='RG': #0
                visited[r][c]='RG'
            else:
                visited[r][c]='B'
            sol(r,c,rgb)
    return

cnt=0
cnt2=0
for i in range(x):
    for j in range(x):
        if visited[i][j]==0:
            sol(i,j,mat[i][j]) # 0
            cnt+=1

mat=visited
visited=[[0]*x for i in range(x)]

for i in range(x):
    for j in range(x):
        if visited[i][j]==0:
            sol(i,j,mat[i][j]) # 0
            cnt2+=1
print(cnt, cnt2)
