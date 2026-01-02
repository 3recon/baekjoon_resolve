from collections import deque

n,m=map(int,input().split())

graph=[[] for i in range(n+1)]

for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

rel=[0]*n

def bfs(x):
    truefalse=set()
    truefalse.add(x)
    visited=[0]*(n+1)
    dq=deque([x])
    while dq:
        cur=dq.popleft()

        for neighbor in graph[cur]:
            if neighbor not in truefalse:
                dq.append(neighbor)
                truefalse.add(neighbor)
                visited[neighbor]=visited[cur]+1
    s=sum(visited)
    return s



for i in range(1,n+1):
    rel[i-1]=bfs(i)
smallest=0
print(rel)
for i in range(len(rel)):
    if rel[smallest]>rel[i]:
        smallest=i
print(smallest+1)