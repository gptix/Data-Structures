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
    """A singly linked list of zero or more Nodes."""
    def __init__(self):
        """Initially has an empty head (ditzy)."""
        # anchor node
        self.head = None
        
    def __str__(self):
        return (f'<Linked List>')
        
    def add(self, value):
        """An element is added to the list by constructing
        a new node containing the received value."""
        # value is a number not yet wrapped in a node
        new_node = Node(value)

        # case - list is empty
        if not self.head:
            self.head = new_node
        
        else: # A head node exists.
#             print(f'self.head: {self.head} - next node: {self.head.next_node}') # store
            next = self.head
            self.head = new_node
#             print(f'self.head: {self.head} - next node: {self.head.next_node}')
            self.head.set_next(next) # use stored
#             print(f'self.head: {self.head} - next node: {self.head.next_node}')
            
    def remove(self):
        if not self.head:
            print("Nothing to pop.")
            return None
            
        else:
#             print(f'head: {self.head} - value: {self.head.value}')
            val = self.head.get_value()
            self.head = self.head.get_next()
            return val