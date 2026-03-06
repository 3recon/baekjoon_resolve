t=int(input())

l=[1,1]

if l==1 or l==2:
    print(1)
else:
    for i in range(2,t):
        b=l[i-1]+l[i-2]
        l.append(b)
    print(l[-1])