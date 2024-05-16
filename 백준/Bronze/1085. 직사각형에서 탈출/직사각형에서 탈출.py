import sys
input=sys.stdin.readline
x,y,w,h=map(int,input().split())
a=w-x
b=h-y
judge_list=[x,y,a,b]
result=min(judge_list)
print(result)