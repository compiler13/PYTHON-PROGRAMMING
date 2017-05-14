
n=int(input())

li=list(map(int,input().split()))




li=sorted(li)

while(n-1>-1):

    if li[n-1]>li[n-2]:

        print(li[n-2])
        break

    else:
        n=n-1
    


    
