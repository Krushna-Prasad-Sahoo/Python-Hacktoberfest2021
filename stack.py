# implementing the stack data structure using the python list

# Basic Code For Undestanding The Stack

# create empty list
stack = []

# stack follows the LIFO : Last In First Out

# push operation on stack : add elements at the end
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
# now the stack looks like this
# [10,20,30]

# pop operation on stack : remove the elements at the end
stack.pop()
stack.pop()
stack.pop()

print(stack)
# now the stack is empty because ll the elemnts removed
# []


# IMPLEMENTING STACK OPERATIONS
stack = []


def push():
    element = input("enter the element")
    stack.append(element)
    print(stack)


def pop_elment():
    if not stack:
        print("the stack is empty")

    else:
        e = stack.pop()
        print("removed element", e)
        print(stack)


while True:
    print("the select the operation 1.push 2.pop 3.quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()

    elif choice == 3:
        break

    else:
        print("please select valid operation")
