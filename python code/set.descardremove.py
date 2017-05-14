n = int(input())

st = set(map(int,input().split()))

ins = int(input())

for i in range(ins):

    inst=input().split()
    if inst[0]=='pop':
        st.pop()
    elif inst[0]=='remove':
        st.remove(int(inst[1]))

    elif inst[0]=='discard':
        st.discard(int(inst[1]))



print(sum(st))


