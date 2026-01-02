import sys
from collections import deque
input=sys.stdin.readline

a,b=map(int,input().split())

# visited=[1]*(b+1)
visited=bytearray(b+1) ##bytearray는 처음 봄,, 이거 썼는데도 메모리 터질 뻔함
def bfs(x):
    dq=deque([x])
    cnt=0
    while dq:
        cur=dq.popleft()

        if int(cur)==b:
            return visited[cur]+1

        for oper in (cur*2, int(str(cur)+"1")):
            if int(oper)<=b:
                s=visited[cur]+1
                visited[oper]=s
                dq.append(int(oper))
    return -1

print(bfs(a))