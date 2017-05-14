

n=int(input())
li=[]

for i in range(n):

    s=input().split()

    if s[0]==('insert'):

        li.insert(int(s[1]),int(s[2]))
    elif s[0]==('remove'):

                  li.remove(int(s[1]))

    elif s[0]==('append'):

                  li.append(int(s[1]))

    elif s[0]==('sort'): 

                li.sort()


    elif s[0]==('pop'):
                  li.pop()


    elif s[0]==('reverse'):

                  li.reverse()

    elif s[0]==('print'):

                      print(li)
                  
    
