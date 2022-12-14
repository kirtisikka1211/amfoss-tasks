c=int(input())
n=int(1)
fnlist=[]
mana=int(0)
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
    ele=int(0)
    for ele in range (0,lenA-1):
        ele1=A[ele]
        ele2=A[ele+1]
        if ele1==0:
            g=int(0)
            for ele in range (0,lenA-1):
                eleO=A[ele]
                if eleO>0:
                    g=g+1
            mana=g+1
            break
        elif ele1==ele2:
            mana=lenA
            break
        else:
            mana=lenA+1
    fnlist.append(mana)
    n=n+1

for x in fnlist:
    print (x)
