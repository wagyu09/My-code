def factorization(N):
    factor = 2
    result = []
    while True:
        if N==1: break
        if N%factor==0:
            N=N/factor
            result.append(factor)
        elif N%factor!=0:
            factor+=1
    return result
count=0
def find_prime_number(input_list):
    global count
    if len(input_list)==1: count+=1
    else: return None
N=int(input())
num_list=list(map(int,input().split()))
for i in num_list:
    find_prime_number(factorization(i))
print(count)
