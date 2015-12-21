from stack import Stack

class SetOfStacks(object):

    MAX_STACK_SIZE = 10

    def __init__(self):
        self.stacks = []
        self.stacks.append(Stack())

    def pop(self):
        if len(self.stacks[-1].lst) >= 1:
            return self.stacks[-1].pop()
        elif len(self.stacks[-1].lst) == 0 and len(self.stacks) > 1:
            self.stacks = self.stacks[:-1]
            return self.stacks[-1].pop()
        return "error"

    def pop_at(self, i):
        try:
            return self.stacks[i].pop() 
        except:
            print "invalid pop_at"

    def push(self, data):
        if len(self.stacks[-1].lst) >= SetOfStacks.MAX_STACK_SIZE:
            self.stacks.append(Stack())
        self.stacks[-1].push(data)

def main():
    my_set_of_stacks = SetOfStacks()
    for i in range(100):
        my_set_of_stacks.push(i)
    print my_set_of_stacks.pop_at(5)

main()
