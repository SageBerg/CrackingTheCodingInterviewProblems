from linked_list import LinkedList

ll = LinkedList()
ll.push("a")
ll.push("b")
ref = ll.tail
ll.push("c")

def delete_node(ref):
    ref.data = ref.nxt.data
    ref.nxt = ref.nxt.nxt

delete_node(ref)

node = ll.head
while node != None:
    print node.data
    node = node.nxt
