stack=[]
def push():
    if len(stack)==n:
        print("The stack is full!")
    else:
        element=input("Enter the element:")
        stack.append(element)
        print(stack)
def pop():
    if len(stack)==0:
        print(" The stack is Empty!")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)
n=int(input("Enter the n value!:"))
while True:
    print("Select the operation 1.push 2.pop 3.break")
    choise=int(input())
    if choise==1:
        push()
    elif choise==2:
        pop()
    elif choise==3:
        break
    else:
        print("Enter the correct operation")
