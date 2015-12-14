from linked_list import LinkedList
from random import randint

ll = LinkedList()
for i in range(10):
    ll.push(chr(randint(97, 122)))

node = ll.head
i = 0
while node != None:
    i += 1
    print node.data
    node = node.nxt

k = randint(1, 10)
print k

j = 0

node = ll.head
while node != None:
    if i - k == j:
        print node.data
    node = node.nxt
    j += 1
