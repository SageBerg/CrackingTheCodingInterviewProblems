from tree import Node
from linked_list import LinkedList

def fill_linked_lists_dict(node, lists_dict, depth):
    if node == None:
        return
    if depth not in lists_dict:
        lists_dict[depth] = LinkedList()
        lists_dict[depth].push(node.data)
    else:
        lists_dict[depth].push(node.data)
    fill_linked_lists_dict(node.left, lists_dict, depth + 1)
    fill_linked_lists_dict(node.right, lists_dict, depth + 1)

def main():
    root = Node(0)
    root.left = Node(-2)
    root.left.right = Node(-1) 
    root.right = Node(1)
    root.right.right = Node(2)
    lists_dict = dict()
    fill_linked_lists_dict(root, lists_dict, 0)
    i = 0
    while i in lists_dict:
        lst = lists_dict[i]
        ll_node = lst.head
        while ll_node != None:
            print ll_node.data
            ll_node = ll_node.nxt
        i += 1
        print

main()
