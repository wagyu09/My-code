import sys
input = sys.stdin.readline
stack=[]
num=int(input())

for _ in range(num):
    usr_input=input()
    usr_input=list(usr_input.split())
    if 'push' in usr_input:
        stack.append(usr_input[-1])
    elif 'top' in usr_input:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif 'size' in usr_input:
        print(len(stack))
    elif 'empty' in usr_input:
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif 'pop' in usr_input:
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())