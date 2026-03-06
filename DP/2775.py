t=int(input())

for i in range(t):
    k=int(input())
    n=int(input())

    lst=[[0]* (n+1) for i in range(k+1)]
    
    for j in range(1,n+1):
        lst[0][j]=j
    
    for j in range(1,k+1):
        for l in range(1,n+1):
            lst[j][l]=sum(lst[j-1][:l+1])
    print(lst[k][n])