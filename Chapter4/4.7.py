from tree import Node

def get_common_ancestor(node_1, node_2):
    height_1 = get_height(node_1, 0)
    height_2 = get_height(node_2, 0)
    if height_1 > height_2:
        moves = abs(height_1 - height_2)
        while moves > 0:
            node_1 = node_1.parent
            moves -= 1
    if height_2 > height_1:
        moves = abs(height_2 - height_1)
        while moves > 0:
            node_2 = node_2.parent
            moves -= 1
    while node_1 is not node_2:
        node_1 = node_1.parent
        node_2 = node_2.parent
    return node_1.data

def get_height(node, height):
    if node.parent == None:
        return height
    return get_height(node.parent, height + 1)

def main():
    root = Node(0)
    root.set_right(10)
    root.right.set_right(20)
    root.right.set_left(5)
    root.set_left(-10)
    print get_common_ancestor(root.right.right, root.right.left)

main()
