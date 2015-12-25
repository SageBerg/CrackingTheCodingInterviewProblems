from tree import Node

def count_sums(node, count, target):
    if node == None or node.data > target:
        return
    if node.data == target:
        count[0] += 1
    elif node.data < target:
        count_sums(node.left, count, target - node.data)
        count_sums(node.right, count, target - node.data)

def count_all_sums(node, count, target):
    if node == None:
        return
    count_sums(node, count, target)
    count_all_sums(node.left, count, target)
    count_all_sums(node.right, count, target)

def main():
    root = Node(1)
    root.set_left(1)
    root.left.set_left(2)
    root.left.set_right(1)
    root.set_right(2)
    root.right.set_left(1)
    root.right.set_right(1)
    root.right.left.set_left(2)
    count = [0]
    count_all_sums(root, count, 2)
    print count

main()
