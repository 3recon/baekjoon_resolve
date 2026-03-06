t=int(input())

l=0
r=1
x=0
for i in range(1,t):
    x=l+r
    l=r
    r=x
print(r)