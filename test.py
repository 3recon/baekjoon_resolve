from collections import deque
import sys
input=sys.stdin.readline


def bfs(s1,s2):
    dq=deque([[s1,s2]])

    while dq:
        cur=dq.popleft()
        x=cur[0]
        y=cur[1]
        moves=[(x+2,y+1),(x+2,y-1),(x-2,y+1),(x-2,y-1),(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2)]
        
        if x==end1 and y==end2:
            return matrix[x][y]
        for move1,move2 in moves:
            if 0<=move1<leng and 0<=move2<leng and matrix[move1][move2]==0:
                matrix[move1][move2]=matrix[x][y]+1
                dq.append([move1,move2])



n=int(input())
for i in range(n):
    leng=int(input())
    matrix=[[0 for j in range(leng)]for h in range(leng)]

    start1,start2=map(int,input().split())
    end1,end2=map(int,input().split())
    print(bfs(start1,start2))

