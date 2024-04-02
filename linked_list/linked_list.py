
# TODO: 
# 1.   Create a method to retrieve an element from a specific position: get(i) or even llist[i].
# 2.    Create a method to reverse the linked list: llist.reverse().
# 3.    Create a Queue() object inheriting this article’s linked list with enqueue() and dequeue() methods.


class Node:
    def __init__(self, data):
        self.data = data
        self.next: None | Node = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head: None | Node = None
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
        # print(nodes)
        return " -> ".join(nodes)

    def __iter__(self):
        """
        Iterating over elements in the linked list.
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node: Node) -> None:
        """
        This method is the advantage of the linked list.
        It is done in O(1), since we store the beginning the
        linked list and we just need to update pointers.
        """
        node = Node(node)
        node.next = self.head
        self.head = node
    
    def add_last(self, node) -> None:
        """
        Adding last takes O(n) because we need to iterate
        over whole linked list, find the last element and add after it.
        """
        print("Inserting in the end:", node)
        node = Node(node)
        if self.head is None:  # if linked list is empty
            self.head = node
            return
        for current_node in self:
            print("current node:", current_node)
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        """
        This method also takes O(n) because we need to iterate
        over unknown amount of elements before we reach required element,
        and insert new element after it.
        """
        if self.head is None:
            raise Exception("List is empty")
        
        new_node = Node(new_node)
        for node in self:
            if node.data == target_node_data:  # look for the node to add after
                new_node.next = node.next  # adding next value as the current node
                node.next = new_node  # add next value after target_node as the new_node
                return

        raise IndexError(f"Node with data {target_node_data} not found") 
    
    def add_before(self, target_node_data, new_node):
        if self.head is None:  # linked list is empty
            raise IndexError("List is empty")

        # if head is required element, simply call add_first to
        # add before the head
        if self.head.data == target_node_data:
            return self.add_first(new_node)

        new_node = Node(new_node)    
        prev_node: Node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        
        raise IndexError(f"Node with data '{target_node_data}' not found")
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise IndexError("List is empty")
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        
        previous_node: Node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        
        raise IndexError(f"Node with data '{target_node_data}' not found")

    def __getitem__(self, index) -> str:
        """
        O(n) method to access values in linked list by index.
        """
        if self.head is None:
            raise IndexError("List is empty")
        count = 0
        for node in self:
            if count == index:
                return node.data
            count += 1
        
        raise IndexError(index)
        
        

if __name__ == "__main__":
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

    ## iterating over linked list
    # llist = LinkedList(["a", "b", "c", "d", "e"])
    # print(llist)

    # for node in llist:
    #     print(node)

    ## inserting in the beginning
    # llist = LinkedList()
    # llist.add_first("b")
    # print(llist)

    # llist.add_first("a")
    # print(llist)

    ## insterting in the end
    # llist = LinkedList(["a", "b"])
    # llist.add_last("c")
    # print(llist)
        
    ## inserting after
    # LinkedList().add_after("b", "a")  # List is empty
    # LinkedList(["a"]).add_after("b", "c")  # IndexError: Node with data b not found

    # llist = LinkedList(["a", "c"])
    # print(llist)
    # llist.add_after("a", "b")
    # print(llist)

    ## inserting before
    # LinkedList().add_before("b", "c")  # IndexError: List is empty
    # LinkedList(["b"]).add_before("c", "d") # IndexError: Node with data 'c' not found

    # add if the target_data == head
    # llist = LinkedList(["b"])
    # print(llist)
    # llist.add_before("b", "a")
    # print(llist)

    # llist = LinkedList(["a", "c"])
    # print("llist before:", llist)
    # llist.add_before("c", "b")
    # print("llist after:", llist)

    ## removing node
    # LinkedList().remove_node("a")  # IndexError: List is empty

    # delete in the beginning
    llist = LinkedList(["a", "b", "c"])
    print("llist before", llist)
    llist.remove_node("a")
    print("llist after:", llist)

    # delete in the middle
    llist = LinkedList(["a", "b", "c"])
    print("llist before", llist)
    llist.remove_node("b")
    print("llist after:", llist)