

li=[]

n=int(input())

for i in range(n):

    s=input()

    a=float(input())

    li.append([s,a])





ans=sorted(list(set([a for s,a in li])))[1]


print('\n'.join([s for s,a in sorted(li) if a==ans]))
