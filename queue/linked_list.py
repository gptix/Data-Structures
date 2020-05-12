class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # anchor node
        self.head = None

    def add(self, value):
        # value is a number not yet wrapped in a node
        new_node = Node(value)
        hed = self.head

        # case - list is empty
        if not hed:
            hed = new_node

        else: # head exists
            old_head_next = hed.next_node
            hed = new_node
            hed.next_node = old_head_next
            



        # case
