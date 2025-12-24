import heapq
import sys

input=sys.stdin.readline
n=int(input())
hq=[]

for i in range(n):
    x=int(input())
    if x:
        heapq.heappush(hq,(abs(x),x))   
        print(hq)
        
    else:
        if hq:
            print(heapq.heappop(hq)[1])

        else:
            print(0)