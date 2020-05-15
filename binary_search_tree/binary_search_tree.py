from collections import deque

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, target):
        if target < self.value: # should I look left, or right?
            if not self.left:
                self.left = BSTNode(target)  # add node as left child
            else: 
                self.left.insert(target) # recurse left
        else: # target is >= self.value, look right
            if not self.right:
                self.right = BSTNode(target) # add node as right child
            else:
                self.right.insert(target) # recurse right

                    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else: 
            if self.right:
                return self.right.contains(target)
            else:
                return False    # Return the maximum value found in the tree

            
    def get_max(self):
        vals = [self.value]
        if self.left:
            vals.append(self.left.get_max())
        if self.right:
            vals.append(self.right.get_max())
        return max(vals)
    
      
    # Call the function `fn` on the value of each node
    # [Jud] - I suppose we should return the results
    def for_each(self, fn):
        return_node = BSTNode(fn(self.value))
        if self.left: 
            return_node.left = self.left.for_each(fn)
        if self.right: 
            return_node.right = self.right.for_each(fn)
        return return_node
    
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()
            
            
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = deque()

        q.append(self)
        
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
                
            print(current_node.value)
            
            
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stk = []
#         print(f'stack length: {len(stk)}')
        stk.append(self)
#         print(f'stack length: {len(stk)}')

        
        while len(stk) > 0:
            curr = stk.pop()
#             print(f'stack length: {len(stk)}')
            if curr.right:
                stk.append(curr.right)
#                 print('added right to stack')
#                 print(f'stack length: {len(stk)}')
            if curr.left:
                stk.append(curr.left)
#                 print('added left to stack')
#                 print(f'stack length: {len(stk)}')
                
            print(curr.value)

# foo = BSTNode(10)
# foo.insert(1)
# foo.insert(20)
# foo.insert(15)

# foo.dft_print()