import sys
input = sys.stdin.readline
A,B=map(int,input().split())
def maximum_common(num1,num2):
    num_list=[num1,num2]
    max_value=max(num_list)
    min_value=min(num_list)
    temp=max_value % min_value
    if temp==0:
        return min_value
    else:
        return maximum_common(min_value,temp)
def minimum_common(num1,num2):
    return int((num1*num2)/maximum_common(num1,num2))


print(maximum_common(A,B))
print(minimum_common(A,B))
