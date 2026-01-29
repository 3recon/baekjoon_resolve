import sys
input = sys.stdin.readline
from collections import deque

n,m,r=map(int,input().split())

adj=[[] for i in range(n+1)]

for i in range(m):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

visited=[0]*(n+1)
def sol(r):
    rank=1
    dq=deque([r])
    visited[r]=rank
    while dq:
        cur=dq.popleft()
        adj[cur].sort(reverse=True)
        for neighbor in adj[cur]:
            if visited[neighbor]==0:
                rank+=1
                visited[neighbor]=rank
                dq.append(neighbor)

sol(r)
for i in range(1,n+1):
    print(visited[i])