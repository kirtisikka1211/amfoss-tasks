c=int(input())
n=1
fnlist=[]
for n in range(0,c):
    N=int(input())
    A= list(map(int,input().strip().split()))[:N]
    while A[0]==0 :
        A.pop(0)
    Alen=len(A)
    g=0
    h=0
    for x in range (0,Alen-1):
        if A[x]==0:
            g=g+1
    for y in range (0,Alen-1):
        h=h+A[y]
    fnlist.append(g+h)

for z in fnlist:
    print (z)
