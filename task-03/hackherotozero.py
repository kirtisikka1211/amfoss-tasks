c=int(input())
n=int(1)
fnlist=[]
manan=int(0)
if c<=0:
    c=int(input())

for n in range(0,c):
    N=int(input())
    A= list(map(int,input().strip().split()))[:N]
    A.sort()
    lenA=len(A)
    if lenA<N:
        H=N-lenA
        for l in range (1,H):
            A.append(0)
    A.sort()
    elem=int(0)
    for elem in range (0,lenA-1):
        elem1=A[elem]
        elem2=A[elem+1]
        if elem1==0:
            g=int(0)
            for elem in range (0,lenA-1):
                elemO=A[elem]
                if elemO>0:
                    g=g+1
            manan=g+1
            break
        elif elem1==elem2:
            manan=lenA
            break
        else:
            manan=lenA+1
    fnlist.append(manan)
    n=n+1

for x in fnlist:
    print (x)