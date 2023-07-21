class Node:
    def __init__(self, prev, next, val):
        self.prev = prev
        self.next = next
        self.val = val



class LRUCache:

    def __init__(self, capacity: int):
        self.LRU = None
        self.MRU = None
        self.keyToNode = {} # key -> nodes
        

    def get(self, key: int) -> int:



    def put(self, key: int, value: int) -> None:
        
        if len(keyToNode) == 0:
            newNode = Node(None, None, value)
            self.LRU = newNode
            self.MRU = newNode
            self.keyToNode[key] = newNode
        elif key in self.keyToNode:
            keyToNode = self.keyToNode[key]
            keyToNode.val = value
            if keyToNode.prev:
                keyToNode.prev.next = keyToNode
            if keyToNode.next:
                keyToNode.next.prev = keyToNode.prev



            