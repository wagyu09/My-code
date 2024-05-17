from StackClass import ArrayStack
stack = ArrayStack(100)
msg=input("문자열 입력: ")
for i in msg:
    stack.push(i)

print('문자열 출력: ',end='')
while not stack.isEmpty():
    print(stack.pop(), end='')
print(stack.peek())