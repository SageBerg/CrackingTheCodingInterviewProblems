from linked_list import LinkedList

def is_palindrome(ll):
    new_ll = LinkedList()

    length = 0
    node = ll.head
    while node != None:
        new_ll.prepend(node.data)
        length += 1
        node = node.nxt

    node = ll.head
    comp_node = new_ll.head
    distance_into_list = 0
    while node != None and comp_node != None and \
            distance_into_list <= length / 2:
        if comp_node.data != node.data:
            return False
        node = node.nxt
        comp_node = comp_node.nxt
    return True

ll1 = LinkedList()
ll1.push("a")
ll1.push("b")
ll1.push("b")
ll1.push("a")
print is_palindrome(ll1)

ll2 = LinkedList()
ll2.push("a")
ll2.push("b")
print is_palindrome(ll2)
