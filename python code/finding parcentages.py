
n= int(input())

dict={}

for i in range(n):

    s=input().split()

    scor=list(map(float,s[1:]))

    avg=sum(scor)/float(len(scor))

    dict[s[0]]=avg


person=input()

print("%.2f"% dict[person])
