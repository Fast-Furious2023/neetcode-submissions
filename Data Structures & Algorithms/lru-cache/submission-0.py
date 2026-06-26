class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    

    def __init__(self, capacity: int):
        #hashmap for key-node pairs, for O(1) lookup
        self.cache = {}
        self.capacity = capacity

        #doublylinked list for key, value, for O(1) remove and re-insert, and tracking MRU
        self.right = Node()
        self.left = Node()
        self.right.prev = self.left
        self.left.next = self.right

    #remove node from linkedlist
    def remove(self, node):
        prevN=node.prev
        nextN=node.next
        prevN.next = nextN
        nextN.prev = prevN

    #insert node into linkedlist at the right=most recently used
    def insert(self, node):
        prevN = self.right.prev
        prevN.next = node
        node.prev = prevN
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        
        #reorder linkedlist
        self.remove(node)
        
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.insert(node) # re-insert node
        self.cache[key]=node#update cache
        if len(self.cache) > self.capacity:
            node = self.left.next #real node to be moved, least recently used, at the left
            self.remove(node)
            del self.cache[node.key]


        
