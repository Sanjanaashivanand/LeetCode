import heapq
from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

class MaxStack:
    def __init__(self):
        self.head = Node(0)  # Dummy head
        self.tail = Node(0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

        self.valToNodes = defaultdict(list)
        self.maxHeap = []

    def _add_node(self, node):
        """Add node to the DLL just before tail"""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def _remove_node(self, node):
        """Remove node from DLL"""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def push(self, x):
        node = Node(x)
        self._add_node(node)
        self.valToNodes[x].append(node)
        heapq.heappush(self.maxHeap, -x)

    def pop(self):
        if self.head.next == self.tail:
            return None

        node = self.tail.prev
        self._remove_node(node)
        self.valToNodes[node.val].pop()
        return node.val

    def top(self):
        return self.tail.prev.val

    def peekMax(self):
        while self.maxHeap:
            max_val = -self.maxHeap[0]
            if self.valToNodes[max_val]:
                return max_val
            heapq.heappop(self.maxHeap)  # Lazy cleanup
        return None

    def popMax(self):
        max_val = self.peekMax()
        node = self.valToNodes[max_val].pop()
        self._remove_node(node)
        return max_val
