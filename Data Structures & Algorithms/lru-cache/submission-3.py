class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left = Node(0, 0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prevNode = self.right.prev
        prevNode.next = node
        node.prev = prevNode
        self.right.prev = node
        node.next = self.right

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            nodeToRemove = self.left.next
            self.remove(nodeToRemove)
            del self.cache[nodeToRemove.key]
