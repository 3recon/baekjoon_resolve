n=int(input())
a,b=1,2

if n<=2:
    print(n)
else:
    for i in range(2,n):
        temp=b
        b+=a
        a=temp
    print(b%10007)