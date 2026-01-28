import sys
input=sys.stdin.readline
from collections import deque


def sol(y,x):
    moves=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]
    #상,우,하,좌,2시,10시,7시,4시
    dq=deque([(y,x)])
    while dq:
        cur=dq.popleft()
        cur_y=cur[0]
        cur_x=cur[1]
        for move1,move2 in moves:
            now_x,now_y=cur_x+move1,cur_y+move2
            if 0<=now_x<w and 0<=now_y<h:
                if adj[now_y][now_x]==1:
                    if visited[now_y][now_x]==0:
                        visited[now_y][now_x]=1
                        dq.append((now_y,now_x))

    


while True:
    w,h=map(int,input().split())
    cnt=0
    if w==0 and h==0:
        break
    adj=[]
    visited=[[0]*w for i in range(h)]
    for i in range(h):
        row=list(map(int,input().split()))
        adj.append(row)
    for i in range(h):
        for j in range(w):
            if adj[i][j]==1 and visited[i][j]==0:
                visited[i][j]=1
                sol(i,j)
                cnt+=1
    print(cnt)