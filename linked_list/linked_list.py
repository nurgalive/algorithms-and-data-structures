class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        """
        This method is the advantage of the linked list.
        """
        node.next = self.head
        self.head = node


# llist = LinkedList()
# print(llist)


# first_node = Node("a")
# llist.head = first_node
# print(llist)


# second_node = Node("b")
# third_node = Node("c")
# first_node.next = second_node
# second_node.next = third_node
# print(llist)

llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)

for node in llist:
    print(node)
