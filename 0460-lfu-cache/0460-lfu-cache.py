from collections import defaultdict

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def len(self):
        return self.size

    def add(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head
        self.size += 1

    def remove(self, node):
        if self.size == 0:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_tail(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node

class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.minfreq = 0
        self.key_value_map = {}
        self.freq_map = defaultdict(DLinkedList)

    def update(self, node):
        freq = node.freq
        self.freq_map[freq].remove(node)

        if self.minfreq == freq and self.freq_map[freq].len() == 0:
            self.minfreq += 1

        node.freq += 1
        self.freq_map[node.freq].add(node)

    def get(self, key):
        if key not in self.key_value_map:
            return -1

        node = self.key_value_map[key]
        self.update(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.key_value_map:
            node = self.key_value_map[key]
            node.value = value
            self.update(node)
        else:
            if self.size == self.capacity:
                lfu_list = self.freq_map[self.minfreq]
                node_to_remove = lfu_list.remove_tail()
                del self.key_value_map[node_to_remove.key]
                self.size -= 1

            new_node = Node(key, value)
            self.key_value_map[key] = new_node
            self.freq_map[1].add(new_node)
            self.minfreq = 1
            self.size += 1
