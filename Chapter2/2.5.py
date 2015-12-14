from linked_list import LinkedList
from random import randint

ll1 = LinkedList()
ll2 = LinkedList()
number_string1 = ""
number_string2 = ""
for i in range(3):
    roll1 = randint(0, 9)
    roll2 = randint(0, 9)
    number_string1 += str(roll1)
    number_string2 += str(roll2)
    ll1.push(roll1)
    ll2.push(roll2)
print(number_string1)
print(number_string2)

def add_lists(ll1, ll2):
    number_string_1 = ""
    number_string_2 = ""
    node = ll1.head
    while node != None:
        number_string_1 += str(node.data)
        node = node.nxt
    node = ll2.head
    while node != None:
        number_string_2 += str(node.data)
        node = node.nxt
    return int(number_string_1) + int(number_string_2)

def rev_add(node):
    if node.nxt == None:
        return str(node.data) 
    return rev_add(node.nxt) + str(node.data)

print add_lists(ll1, ll2);
print rev_add(ll1.head), rev_add(ll2.head) 
print int(rev_add(ll1.head)) + int(rev_add(ll2.head))
