#stack implementation
def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def push(stk,item):
    stk.append(item)
    top=len(stk)-1
def pop(stk):
    if isEmpty(stk):
        return "underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
def peek(stk):
    if isEmpty(stk):
        return 'underflow'
    else:
        return len(stk)-1
def display(stk):
    if isEmpty(stk):
        print('Stack is empty')
    else:
        print(stk[top],'---> top')
        for a in range(top-1,-1,-1):
            print(stk[a])
#main
stack=[]
top=0
while True:
    print("stack operation:\n  1 push\n  2 pop\n  3 peek\n 4 dispaly stack\n 5 exit\n")
    ch=int(input('Enter your choice'))
    if ch==1:
          item=input('Enter element')
          push(stack,item)
    elif ch==2:
        item=pop[stack]
        if item=='underflow':
            print('underflow stack is empty')
        else:
            print('popped item is',item)
    elif ch==3:
        item=peek(stack)
        if item=='underflow':
            print('underflow stack is empty')
        else:
            print('the topmost item is', item)
    elif ch==4:
        display(stack)
    elif ch==5:
        break
    else:
        print('invalid choice')





























          
