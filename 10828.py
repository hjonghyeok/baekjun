import sys

n=int(sys.stdin.readline().rstrip())

stack=[]

def stact_push(stack, value):
    stack.append(value)
    return stack

def stact_pop(stack):
    return stack.pop()

def stact_size(stack):
    return len(stack)

def stact_empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
def stact_top(stack):
    return stack[len(stack)-1]

m,k=map(str,sys.stdin.readline().rstrip().split())
if m=='push':
    stact_push(stack,int(k))
elif m=='pop':
    stact_pop(stack)
elif m[0]=='size':
    print(stact_size(m[1:]))
elif m[0]=='empty':
    print(stact_empty(m[1:]))
elif m[0]=='top':
    print(stact_top(m[1:]))