from collections import deque
a,p=map(int,input().split())
i=1
power=[a]

while True:
    a=str(a)
    a_lst=[[i for i in a]]
    cur=a_lst.pop()
    s=0
    for a in cur:    
        a=int(a)
        s+=a**p
    a=s
    i+=1
    if s not in power:
        power.append(s)
    else:
        end=power.index(s)
        print(len(power[0:end]))
        break
    
