n=int(input())

step=1
while n>step:
    n-=step
    step+=1

if step%2==0:
    head=n
    tail=step-n+1
    print(f'{head}/{tail}')
else:
    tail=n
    head=step-n+1
    print(f'{head}/{tail}')