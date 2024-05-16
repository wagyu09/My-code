#2675
T=int(input())
for i in range(T):
    A,B=list(input().split())
    A=int(A[0])
    for s in range(len(B)):
        if s==len(B)-1: print(B[-1]*A,end='\n')
        else: print(B[s]*A,end='')