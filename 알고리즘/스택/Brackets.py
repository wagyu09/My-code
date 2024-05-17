from StackClass import ArrayStack
def checkBrackets(string):
    stack = ArrayStack(100)
    for i in msg:
        if i in ['(','[','{']:
            stack.push(i)
        elif i in [')',']','}']:
            if stack.isEmpty():
                return False
            else:
                left=stack.pop()
                if (i == '}' and left != '{') or\
                   (i == ')' and left != '(') or\
                   (i == ']' and left != '['):
                    return False
    return stack.isEmpty()
msg=input('입력 하세요: ')
print(checkBrackets(msg))