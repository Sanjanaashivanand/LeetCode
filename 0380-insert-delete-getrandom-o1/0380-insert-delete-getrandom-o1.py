import random

class RandomizedSet:
    def __init__(self):
        self.nums = []      # stores actual values
        self.indices = {}   # maps value -> index in nums
    
    def insert(self, val):
        if val in self.indices:
            return False
        
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True
    
    def remove(self, val):
        if val not in self.indices:
            return False
        
        # Swap with last element to avoid shifting
        last_element = self.nums[-1]
        idx_to_remove = self.indices[val]
        
        self.nums[idx_to_remove] = last_element
        self.indices[last_element] = idx_to_remove
        
        # Remove last element
        self.nums.pop()
        del self.indices[val]
        return True
    
    def getRandom(self):
        return random.choice(self.nums)