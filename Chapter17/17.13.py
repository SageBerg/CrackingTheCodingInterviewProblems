class BiNode(object):

    def __init__(self, data):
        self.node_1 = None #left  #prev
        self.node_2 = None #right #next
        self.data = data

def tree_to_list(node):

    if node == None:
        return
    result = tree_to_list(node.node_1) 
    result = tree_to_list(node.node_2)
    if node.node_1 == None and node.node_2 == None:
        node.node_1 = None
    print node.data

def main():
    root = BiNode(10)
    root.node_1 = BiNode(5)
    root.node_2 = BiNode(15)
    tree_to_list(root)

main()
        
