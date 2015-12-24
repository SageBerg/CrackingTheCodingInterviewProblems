from tree import Node

def next_node(start_node, node):
    if start_node.left == None and start_node.right == None:
        if node.parent != None:
            return node.parent.data
        return None
    if node.left != None:
        return next_node(start_node, node.left)
    if node.right != None:
        return next_node(start_node, node.right)
    if node.right == None and node.left == None:
	return node.data

def main():
    root = Node(0)
    root.set_left(-10)
    root.set_right(10)
    root.left.set_right(-5)
    print next_node(root.left, root.left)

    root = Node(0)
    root.set_left(-10)
    root.left.set_right(-5)
    root.left.right.set_left(-7)
    print next_node(root.left, root.left)

main()
