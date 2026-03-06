n=int(input())

lst=[1,1]
if n==1:
    print(4)
elif n==2:
    print(6)    
else:
    for i in range(2,n):
        x=lst[-1]+lst[-2]
        lst.append(x)
    print((lst[-1]+lst[-2])*2 + (lst[-3]+lst[-2])*2 )