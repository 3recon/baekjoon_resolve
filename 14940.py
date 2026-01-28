import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
mat = []

for i in range(n):
    lst = list(map(int, input().split()))
    mat.append(lst)

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[0] * m for i in range(n)]

def sol(r, c):
    dq = deque([(r, c)])

    while dq:
        cur = dq.popleft()
        cur_r = cur[0]
        cur_c = cur[1]

        for move_r, move_c in move:
            shift_r, shift_c = move_r + cur_r, move_c + cur_c
            if 0 <= shift_r < n and 0 <= shift_c < m:  # 크기 조건
                if visited[shift_r][shift_c] == 0 and mat[shift_r][shift_c] != 0:
                    # 방문하지 않은 땅과 막혀있는 땅이 아닌 조건
                    # if visited[shift_r][shift_c] < visited[cur_r][cur_c] + 1 and (shift_r!=r and shift_c!=c):
                    if visited[shift_r][shift_c] < visited[cur_r][cur_c] + 1:
                        visited[shift_r][shift_c]=visited[cur_r][cur_c] + 1
                        dq.append((shift_r, shift_c))

row_2=None
col_2=None
for i in range(n):
    for j in range(m):
        if mat[i][j]==2:
            row_2=i
            col_2=j
            break
sol(row_2,col_2)
visited[row_2][col_2]=0
for v in visited:
    print(*v)
