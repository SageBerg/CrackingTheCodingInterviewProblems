from stack import Stack

class Queue(object):

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, data):
        self.stack_1.push(data)

    def dequeue(self):
        if len(self.stack_2.lst) == 0:
            while len(self.stack_1.lst) > 0:
                self.stack_2.push(self.stack_1.pop())
        return self.stack_2.pop()

def main():
    q = Queue()
    items = 10
    for i in range(items):
        q.enqueue(i)
    for i in range(items / 2):
        print q.dequeue()
    for i in range(items / 2):
        q.enqueue(i)
    for i in range(items):
        print q.dequeue()

main()
