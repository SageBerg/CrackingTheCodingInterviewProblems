from tree import Node

def build_non_min_tree(lst):
    root = None
    for element in lst:
        node = Node(element)
        if root == None:
            root = node
        else:
            place_node(root, node)
    return root

def place_node(cur_node, node_to_be_placed):
    if cur_node.data > node_to_be_placed.data:
        if cur_node.left == None:
            cur_node.left = node_to_be_placed
        else:
            place_node(cur_node.left, node_to_be_placed)
    if cur_node.data <= node_to_be_placed.data:
        if cur_node.right == None:
            cur_node.right = node_to_be_placed
        else:
            place_node(cur_node.right, node_to_be_placed)

def print_tree_in_order(node):
    if node != None:
        print_tree_in_order(node.left)
        print node.data
        print_tree_in_order(node.right)

def build_tree(lst):
    if lst == []:
        return
    middle = len(lst) / 2
    left_list = lst[:middle]
    right_list = []
    if len(lst) > 1:
        right_list = lst[middle + 1:]
    node = Node(lst[middle])
    node.left = build_tree(left_list)
    node.right = build_tree(right_list)
    return node

def get_tree_height(node, height):
    if node == None:
        return height
    return max(get_tree_height(node.left, height + 1),
               get_tree_height(node.right, height + 1))

def main():
    lst_1 = [-1,0,1,2,3,4,6,7,7]
    root = build_tree(lst_1)
    root_2 = build_non_min_tree(lst_1)
    print_tree_in_order(root) 
    print_tree_in_order(root_2) 
    print "height: " + str(get_tree_height(root, 0))
    print "height: " + str(get_tree_height(root_2, 0))

main()
