from stack import Stack

def towers_of_hanoi(n):
    pole_one = Stack()
    for i in range(n)[::-1]:
        pole_one.push(i)
    pole_two = Stack()
    pole_three = Stack()

    moves = 0
    while pole_three.lst != range(n)[::-1]:
        moves += 1

        if pole_one.peek() == 0:
            pole_three.push(pole_one.pop())

            if pole_one.peek() < pole_two.peek():
                pole_two.push(pole_one.pop())
            elif pole_one.peek() > pole_two.peek(): 
                pole_one.push(pole_two.pop())
        else:
            pole_one.push(pole_three.pop())

            if pole_two.peek() < pole_three.peek():
                pole_three.push(pole_two.pop())
            elif pole_two.peek() > pole_three.peek(): 
                pole_two.push(pole_three.pop())
    print moves 

towers_of_hanoi(2)
towers_of_hanoi(3)
towers_of_hanoi(10)
