from doubly_linked_list import DoublyLinkedList as DLL, ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.length = 0
        self.kv_pair_list = DoublyLinkedList()
        self.key_node_dict = {}
        
        
    def __str__(self):
        return (f'<LRU Cache -- limit: {self.limit} -- limit: {self.length} -- length: {self.length}>')
    
    
    
        """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        
        # The key already has a node
        if key in self.key_node_dict:
            node_to_use = self.key_node_dict[key]
            print(value)
            self.kv_pair_list.move_to_front(node_to_use)
            node_to_use.value=value
            
        else: # key does not exist in kv-pairs
            # add pair to head of DLL
            node_to_use = ListNode(value)
            self.key_node_dict[key] = node_to_use
            self.kv_pair_list.add_to_head({key: value})

            
            # If the list is full, discard the tail-end element
            if self.length == self.limit:
                little_dict = self.kv_pair_list.remove_from_tail()
                key_to_discard = [[k,little_dict[k]] for k in little_dict][0][0]
                print(key_to_discard)
                del self.key_node_dict[key_to_discard]
                
            self.length = len(self.key_node_dict)
    

# foo = LRUCache(3)
# print(foo)
# foo.key_node_dict


    

#     """
#     Retrieves the value associated with the given key. Also
#     needs to move the key-value pair to the end of the order
#     such that the pair is considered most-recently used.
#     Returns the value associated with the key or None if the
#     key-value pair doesn't exist in the cache.
#     """
#     def get(self, key):
#         my_list = self.kv_pair_list
#         my_dict = self.access_dict
        
#         if (node_to_use = my_dict['key']):
#             val = my_list.get(node_to_use).value
#             node_to_use.move_to_end()
#         else: val = None
        
#         return val
