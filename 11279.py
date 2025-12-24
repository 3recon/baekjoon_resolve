import sys
import heapq
input=sys.stdin.readline

n=int(input())
heap=[]

for i in range(n):
    x=int(input())
    if x:
        heapq.heappush(heap,(-x,x))
    
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)