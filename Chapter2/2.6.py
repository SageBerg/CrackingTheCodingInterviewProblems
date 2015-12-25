from linked_list import LinkedList

def find_start_of_loop(ll):
    node = ll.head
    nodes = set()
    while node != None:
        if node in nodes:
            return node.data
        else:
            nodes.add(node)
        node = node.nxt

def find_start_of_loop_no_space(ll):
    runner_1 = ll.head
    runner_2 = ll.head
    while runner_1 != None and runner_2 != None:
        runner_1 = runner_1.nxt
        runner_2 = runner_2.nxt
        if runner_2 != None:
            runner_2 = runner_2.nxt
    	if runner_1 is runner_2:
            return runner_1.nxt.data

def main():
    ll = LinkedList()
    ll.push("a") 
    ll.push("b") 
    ll.push("c")
    ll.push("d")
    ll.push("e")
    ll.push("f")
    ll.tail.nxt = ll.head.nxt
    print find_start_of_loop(ll)
    print find_start_of_loop_no_space(ll)

main()
