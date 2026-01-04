# import sys
# input=sys.stdin.readline
# from collections import deque
# start,end=map(int,input().split())
# y=max(start,end)
# visited=bytearray([0]*(y+1))

# def sol(x):
#     dq=deque([x])

#     while dq:
#         cur=dq.popleft()

#         if cur==end:
#             return visited[cur]

#         for i in (cur-1,cur+1,cur*2):
#             if 0<=i<=y:
#                 visited[i]=visited[cur]+1
#                 dq.append(i)

# print(sol(start))

import sys
input=sys.stdin.readline
from collections import deque
start,end=map(int,input().split())
# y=max(start,end)
# visited=bytearray([0]*(end+1))
max=100_000
visited=[0]*(max+1)

def sol(x):
    dq=deque([x])

    while dq:
        cur=dq.popleft()

        if cur==end:
            return visited[cur]

        for i in (cur-1,cur+1,cur*2):
            if 0<=i<=max and visited[i]==0:
                visited[i]=visited[cur]+1
                dq.append(i)

print(sol(start))