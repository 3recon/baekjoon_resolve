from collections import deque
import sys
sys.setrecursionlimit(10**7)

n,m=map(int,input().split())

lst=[[] for i in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    lst[u].append(v)
    # lst[v].append(u)


result=set()
visited=[0]*(n+1)
def dfs(vertex):
    visited[vertex]=1

    for neighbor in lst[vertex]:
        if visited[neighbor]==0:
            dfs(neighbor)

cnt=0
for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)
        cnt+=1
print(cnt)