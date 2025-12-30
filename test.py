#1697 나중에 반드시 다시 풀기!!

from collections import deque

n,k=map(int,input().split())

lst=[0]*100000

def bfs(start):
    dq=deque()
    dq.append(start)
    
    while dq:
        cur=dq.popleft()
        if cur==k:
            return lst[cur]

        for i in (cur-1,cur+1,cur*2):
            if 0<=i<=100000 and lst[i]==0:
                lst[i]=lst[cur]+1
                dq.append(i)

print(bfs(n))