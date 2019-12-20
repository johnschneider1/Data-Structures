class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None


def traverse_list(self):
    if self.start_node is None:
        print("List has no element")
        return
    else:
        n = self.start_node
        while n is not None:
            print(n.item, " ")
            n = n.ref


def insert_at_start(self, data):
    new_node = Node(data)
    new_node.ref = self.start_node
    self.start_node = new_node


def insert_at_end(self, data):
    new_node = Node(data)
    if self.start_node is None:
        self.start_node = new_node
        return
    n = self.start_node
    while n.ref is not None:
        n = n.ref
        n.ref = new_node


def insert_after_item(self, x, data):

    n = self.start_node
    print(n.ref)
    while n is not None:
        if n.item == x:
            break
        n = n.ref
    if n is None:
        print("item not in the list")
    else:
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node


def insert_before_item(self, x, data):
    # In the script below, we check if the list is empty. If it is actually empty,
    # we simply print that the list has no element and return from the function.
    if self.start_node is None:
        print("List has no element")
        return
    # Next, we check if the element is located at the first index. Look at the following script:
    if x == self.start_node.item:
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node
        return

    n = self.start_node
    print(n.ref)
    while n.ref is not None:
        if n.ref.item == x:
            break
        n = n.ref
    if n.ref is None:
        print("item not in the list")
    else:
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node


def insert_at_index(self, index, data):
    if index == 1:
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node
    i = 1
    n = self.start_node
    while i < index-1 and n is not None:
        n = n.ref
        i = i+1
    if n is None:
        print("Index out of bound")
    else:
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node


new_linked_list = LinkedList()

# new_linked_list.insert_at_end(5)
# new_linked_list.insert_at_end(10)
# new_linked_list.insert_at_end(15)

# new_linked_list.traverse_list()

new_linked_list.insert_at_start(20)
