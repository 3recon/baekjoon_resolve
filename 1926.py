from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())

mat=[]
for i in range(n):
    adj=list(map(int,input().split()))
    mat.append(adj)

visited=[[0]*m for i in range(n)]

temp=0

def sol(u,v):
    global temp
    moves=((u+1,v),(u-1,v),(u,v+1),(u,v-1))

    for n1,n2 in moves:
        if 0<=n1<n and 0<=n2<m:
            if mat[n1][n2]==1 and visited[n1][n2]==0:
                visited[n1][n2]=1
                temp+=1
                sol(n1,n2)
                
    
max_area=0

cnt=0
for i in range(n):
    for j in range(m):
        if mat[i][j]==1 and visited[i][j]==0:
            temp=1
            visited[i][j]=1
            sol(i,j)
            cnt+=1
            if temp>=max_area:
                max_area=temp
print(cnt)
print(max_area)