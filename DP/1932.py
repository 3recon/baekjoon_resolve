import sys
input=sys.stdin.readline

t=int(input())

tri=[]

for i in range(t):
    x=list(map(int,input().split()))
    tri.append(x)

for i in range(t-2,-1,-1):
    for j in range(len(tri[i])):
        tri[i][j]=max(tri[i+1][j],tri[i+1][j+1])+tri[i][j]
print(tri[0][0])