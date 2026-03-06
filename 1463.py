# 백준 1463
from collections import deque

n = int(input())

lst=[0]*(n+1)

def sol(start):
    dq=deque([start])
    while dq:
        cur=dq.popleft()
       
        if cur==1:
            return lst[cur]
        
        if cur%3==0:
            if lst[cur//3]>lst[cur]+1 or lst[cur//3]==0:
                lst[cur//3]=lst[cur]+1
                dq.append(cur//3)
        
        if cur%2==0:
            if lst[cur//2]>lst[cur]+1 or lst[cur//2]==0:
                lst[cur//2]=lst[cur]+1
                dq.append(cur//2)
        
        if lst[cur-1]>lst[cur]+1 or lst[cur-1]==0:
            lst[cur-1]=lst[cur]+1
            dq.append(cur-1)

print(sol(n))