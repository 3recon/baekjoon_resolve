n=int(input())

step=1
while n>step:
    n-=step
    step+=1

head=0
tail=0
if step%2==0:
    head=n
    tail=step-n+1
    print(head,"/",tail)
else:
    tail=n
    head=step-n+1
    print(head,"/",tail)