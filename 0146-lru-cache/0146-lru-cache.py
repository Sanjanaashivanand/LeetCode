class LRUCache(object):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.map = {}

    def add(self, node):
        temp = self.head.next

        self.head.next = node
        node.next = temp

        temp.prev = node
        node.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        
    def get(self, key):
        #Find the element and return; move the accessed to the head
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.add(node)

            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            del self.map[key]

        newNode = self.Node(key, value)
        self.map[key] = newNode

        if len(self.map) > self.capacity:
            last = self.tail.prev
            self.remove(last)
            del self.map[last.key]

        self.add(newNode)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)