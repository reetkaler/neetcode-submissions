# a cache is a small, fast storage area with a size limit
# when its full and something new comes in, something old has to go
# least recently used item is the one that gets deleted
# keep track of how long ago you touched that item

# can remove from a doubly linked list in O(1)
# can also add to the end or remove from the other end in O(1)
# searching in a linked list is O(n) though -> use hashmap for accessing in O(1)

# use a doubly linked list where key value pairs are stored as node
# least recently used node at the head
# most recently used node at the tail
# whenever a key is accessed using get() or put(), remove the corresponding
# node and reinsert at the tail
# when a cache reaches its capacity, remove the LRU node from the head of the list
# use a hash map to store each key and corresponding address of its node

# can just store the node itself as the key in our hashmap entry

# head - least recent
# tail - most recent

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # dummy nodes for head and tail
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # MAKE SURE TO WIRE DUMMY NODES TOGETHER!
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # this key becomes most recently used
        # pop from DLL
        node = self.cache[key]
        self._remove(node)
        self._insert(node)

        return node.val
        
        

    def put(self, key: int, value: int) -> None:
        # update val of the key if exists
        if key in self.cache:
            self._remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key] # make sure to remove lru from cache when fully removing lru

        node = Node(key, value)
        self._insert(node)
        self.cache[key] = node # store node not value
        

    # A B C
    # A -> C
    # C -> C


    def _remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    # A C
    # insert at the tail *REMEMBER DUMMY NODE*
    # A C 0
    # C <-> B
    # B <-> 0
    
    def _insert(self, node) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node



class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
