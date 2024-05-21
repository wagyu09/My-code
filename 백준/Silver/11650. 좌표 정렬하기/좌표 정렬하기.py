N=int(input())
usr_list=[0]*N
for i in range(N):
    a=list(map(int,input().split()))
    usr_list[i]=a
usr_list.sort()
for i in range(len(usr_list)):
    print(usr_list[i][0],end=' ')
    print(usr_list[i][1])