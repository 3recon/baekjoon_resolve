import sys
input = sys.stdin.readline
from collections import deque

n,m,k=map(int,input().split())

matrix=[[-1]*(m+1) for i in range(n+1)]
visited=[[0]*(m+1) for i in range(n+1)]

for i in range(k):
    r,c=map(int,input().split())
    matrix[r][c]=0

moves=[(1,0),(-1,0),(0,1),(0,-1)]

def sol(r,c):
    dq=deque([(r,c)])
    cnt=1

    while dq:
        cur=dq.popleft()
        cur_r=cur[0]
        cur_c=cur[1]

        for mr,mc in moves:
            real_r,real_c=cur_r+mr,cur_c+mc
            if 0<=real_r<n+1 and 0<=real_c<m+1 and visited[real_r][real_c]==0:
                if matrix[real_r][real_c]==0:
                    visited[real_r][real_c]=1
                    dq.append((real_r,real_c))
                    cnt+=1
    return cnt


maximum=0
for row in range(n+1):
    for col in range(m+1):
        if visited[row][col]==0 and matrix[row][col]==0:
            visited[row][col]=1
            temp=sol(row,col)
            if temp>maximum:
                maximum=temp
print(maximum)
