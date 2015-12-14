from linked_list import LinkedList
from random import randint

ll = LinkedList()
for i in range(10):
    ll.push(randint(0, 99))

node = ll.head
while node != None:
    print node.data
    node = node.nxt

def partition(value, ll):
    small = LinkedList()
    large = LinkedList()
    node = ll.head
    while node != None:
        if node.data < value:
            small.push(node.data)
        else:
            large.push(node.data)
        node = node.nxt
    small.tail.nxt = large.head
    small.tail = large.tail
    return small

ll = partition(50, ll)
print

node = ll.head
while node != None:
    print node.data
    node = node.nxt
