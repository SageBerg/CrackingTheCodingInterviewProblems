class Node(object):

    def __init__(self, data):
        self.data = data 
        self.right = None
        self.left = None
        self.parent = None

    def set_left(self, data):
        self.left = Node(data)
        self.left.parent = self

    def set_right(self, data):
        self.right = Node(data)
        self.right.parent = self
