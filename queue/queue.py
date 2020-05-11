"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size # since we have this recorded, don't need to traverse.

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             val = self.storage.pop()
#             self.size -= 1
#             return val

from linked_list import Node, LinkedList

class Queue_ll:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        
    def __len__(self):
        return self.size # since we have this recorded, don't need to traverse.

    def enqueue(self, value):
        self.storage.add(value)
        self.size += 1

    def dequeue(self):
        
        sz = self.size
        
        if sz == 0:
            return None
            
        elif sz > 1:
            next_to_first = self.head
            
            # this pointer to node to be removed forward
            for i in range(1, sz - 1): # if sz == 1, this will not occur
                next_to_first = self.head
                
            val = next_to_first.get_next().get_value()
            next_to_first.set_next(None)
        
        else: # size == 1
            val = head.get_value()
            head = None
            
        size -= 1
        return val
