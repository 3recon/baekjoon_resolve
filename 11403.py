import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import deque

n=int(input())

mat=[]
for i in range(n):
    adj=list(map(int,input().split()))

    mat.append(adj)

print("------------------------------------")


def sol(r):
    dq=deque()
    for i in range(len(mat[r])):
        if mat[r][i]==1:
            dq.append(i)

    visited=[0]*n
    while dq:
        c=dq.popleft()
        visited[c]=1
        for i in range(n):
            if mat[c][i] and visited[i]==0:
                visited[i]=1
                dq.append(i)
    print(*visited)
        

for row in range(n):
    sol(row)
# for x in visited:
#      print(*x)