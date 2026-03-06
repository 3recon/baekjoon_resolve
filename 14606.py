n=int(input())

if n<=1:
    print(0)
else:
    s=0
    result=[n]
    while result:
        t=result.pop()
        x=t//2
        y=t-x
        s+=(x*y)
        if x!=1:
            result.append(x)
        if y!=1:
            result.append(y)
    print(s)