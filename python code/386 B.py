

n=int(input())

s=input()

s1=''

p=n

for i in range(p):

    if(n%2==0):
       
        s1=s[i]+s1

    else:
        s1=s1+s[i]

         

    n=n-1

print(s1)   

   
    
   


    
