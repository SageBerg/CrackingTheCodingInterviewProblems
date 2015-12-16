class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        node = LinkedListNode(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.nxt = self.head
            self.head = node

    def push(self, value):
        node = LinkedListNode(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.nxt = node
            self.tail = node

class LinkedListNode(object):

    def __init__(self, data):
        self.data = data
        self.nxt = None
