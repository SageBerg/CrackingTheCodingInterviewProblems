from tree import Node

def contains_subtree(big_tree_node, order):
    if big_tree_node == None:
        return False
    if big_tree_node.data == order[0]:
        big_order = []
        pre_order(big_tree_node, big_order)
        return big_order == order
    return contains_subtree(big_tree_node.left, order) or \
           contains_subtree(big_tree_node.right, order)    

def pre_order(node, order):
    if node == None:
       return
    order.append(node.data)
    pre_order(node.left, order)
    pre_order(node.right, order)

def main():
    root = Node(0)
    root.set_left(-10)
    root.set_right(10)
    order = []
    pre_order(root, order)

    big_root = Node(100)
    big_root.set_right(0)
    big_root.right.set_left(-10)    
    big_root.right.set_right(10)
 
    print contains_subtree(big_root, order)

main()
