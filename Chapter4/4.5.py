from tree import Node

def is_binary_search_tree(node, min_val, max_val):
     if node == None:
         return True
     if node.data < min_val or node.data > max_val:
         return False
     return is_binary_search_tree(node.left, min(min_val, node.data), node.data) and \
            is_binary_search_tree(node.right, node.data, max(max_val, node.data))

def main():
    root = Node(0)
    root.right = Node(1)
    print is_binary_search_tree(root, -float("inf"), float("inf"))
    root = Node(0)
    root.right = Node(2)
    root.right.left = Node(1)
    root.right.right = Node(1)
    print is_binary_search_tree(root, -float("inf"), float("inf"))

main()
