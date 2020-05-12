"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size # since we have this recorded, don't need to traverse.
    
    def __str__(self):
        print(f'<Stack - storage: {self.storage}>')# - storage head: {self.storage.head}')

    def push(self, value):
        self.storage.add(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            val = self.storage.head.get_value()
            self.size -= 1
            self.storage.remove()
            return val
