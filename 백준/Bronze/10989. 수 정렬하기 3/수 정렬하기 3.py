import sys
input = sys.stdin.readline
temp = [0] * 10001
N = int(input())
for i in range(N):
    usr_input = int(input())
    temp[usr_input] += 1
for i in range(1,10001):
    if temp[i]>0:
        for _ in range(temp[i]):
            print(i)

