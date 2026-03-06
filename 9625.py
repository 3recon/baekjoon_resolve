n=int(input())

acnt,bcnt=1,0
for i in range(n):
    temp=acnt
    acnt+=bcnt
    acnt-=temp
    bcnt+=temp
print(acnt,bcnt)