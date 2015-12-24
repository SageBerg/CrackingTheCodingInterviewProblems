from directed_graph import Node

def is_route_to(cur_node, dest):
    if cur_node is dest:
        return True
    else:
        for link in cur_node.links:
            if is_route_to(link, dest):
                return True
        return False

def main():
    node_1 = Node()
    node_2 = Node()
    node_3 = Node()
    node_4 = Node()
    node_1.links.append(node_2)
    node_2.links.append(node_3)
    node_4.links.append(node_1)
    print is_route_to(node_1, node_1)
    print is_route_to(node_1, node_3)
    print is_route_to(node_1, node_4)

main()
