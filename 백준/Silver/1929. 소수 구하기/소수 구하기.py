import sys
input=sys.stdin.readline
M,N=map(int,input().split())
num_list=[True]*(N+1)
num_list[0],num_list[1]=False,False
for i in range(2,int(N**0.5)+1):
    if num_list[i]:
        for j in range(i*i,N+1,i):
            num_list[j]=False
for i in range(M,N+1):
    if num_list[i]:
        print(i)