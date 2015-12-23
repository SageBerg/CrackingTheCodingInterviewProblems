from tree import Node

def is_balanced(node):
    if node == None:
        return True
    if abs(get_height(node.left, 0) -
           get_height(node.right, 0)) > 1:
        return False
    return True and is_balanced(node.left) and is_balanced(node.right)

def get_height(root, height):
    if root == None:
        return height
    return max(get_height(root.left, height + 1),
               get_height(root.right, height + 1))

def main():
    root = Node(0)
    root.left = Node(1)
    root.left.left = Node(2)
    root.right = Node(1)
    root.right.right = Node(2)
    root.right.right.right = Node(3)
    root.right.left = Node(2)
    print is_balanced(root)

main()
