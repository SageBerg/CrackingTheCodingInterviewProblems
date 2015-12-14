from linked_list import LinkedList
from random import randint

ll = LinkedList()
for i in range(10):
    ll.push(chr(randint(97, 101)))

node = ll.head
while node != None:
    print node.data
    node = node.nxt

node = ll.head
while node != None:
    prev = node
    curr = node.nxt
    while curr != None:
        if curr.data == node.data:
            prev.nxt = curr.nxt
        else:
            prev = curr
        curr = curr.nxt
    node = node.nxt

print
node = ll.head
while node != None:
    print node.data
    node = node.nxt
