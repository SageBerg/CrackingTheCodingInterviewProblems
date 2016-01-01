from stack import Stack
from random import randint

def sort_stack(stack):
    storage_stack = Stack()
    highest = -float("inf")
    stack_length = get_stack_length(stack)

    while stack_length > 0:
        i = 0
        while stack_length != i:
            i += 1
            cur_val = stack.pop()
            if cur_val > highest:
                if highest != -float("inf"):
                     storage_stack.push(highest)
                highest = cur_val
            else:
                storage_stack.push(cur_val)
        stack.push(highest)
        highest = -float("inf")
        stack_length -= 1
        while not storage_stack.is_empty():
            stack.push(storage_stack.pop())

def get_stack_length(stack):
    length = 0
    storage_stack = Stack()
    while not stack.is_empty():
        storage_stack.push(stack.pop())
        length += 1
    while not storage_stack.is_empty():
        stack.push(storage_stack.pop())
    return length

def main():
    my_stack = Stack() 
    for _ in range(10):
        my_stack.push(randint(0, 9))
    sort_stack(my_stack)
    for _ in range(10):
        print my_stack.pop()

main()
