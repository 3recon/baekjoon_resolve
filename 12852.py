from collections import deque
import sys
input=sys.stdin.readline
n=int(input())

def sol(x):
    dq=deque([[x]])

    while dq:
        arr=dq.popleft()
        cur=arr[0]
        if cur==1:
            return arr
        if cur%3==0:
            dq.append([cur//3]+arr)
        if cur%2==0:
            dq.append([cur//2]+arr)
        
        dq.append([cur-1]+arr)

result=sol(n)
print(len(result)-1)
print(*result[::-1])