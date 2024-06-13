N=int(input())
menu=[]
for i in range(N):
    menu.append(int(input()))

M=int(input())
price=0
for i in range(M):
    price+=menu[int(input())-1]
    
print(price)