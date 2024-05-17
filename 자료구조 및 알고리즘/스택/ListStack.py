msg= input('문자열 입력: ')
def stack_with_list(msg):
    stack=list()
    for i in msg:
        stack.append(i)
    print("문자열 출력: ", end='')
    while len(stack) > 0:
        print(stack.pop(), end='')
def stack_with_queue(msg):
    import queue
    stack=queue.LifoQueue(maxsize=100)
    for i in msg:
        stack.put(i)
    print("문자열 출력: ", end='')
    while not stack.empty():
        print(stack.get(), end='')
stack_with_queue(msg)