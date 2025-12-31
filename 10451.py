import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(vertex,visited=None):
    global cnt
    if visited==None:
        visited=set()
    visited.add(vertex)
    
    for neighbor in adjlst[vertex]:
        
        if neighbor not in visited:
            dfs(neighbor,visited)
        else:
            cnt+=1
            for x in adjlst:
                if x and x[0] not in visited:
                    dfs(x[0],visited)
                    

n=int(input())

for i in range(n):
    m=int(input())
    adjlst=[[] for i in range(m+1)]
    lst=list(map(int,input().split()))

    for x in range(m):
        adjlst[x+1].append(lst[x])
    cnt=0
    dfs(1)
    print(cnt)