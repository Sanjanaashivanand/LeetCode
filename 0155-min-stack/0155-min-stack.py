class MinStack(object):
    class Pair:
        def __init__(self, val, mini):
            self.val = val 
            self.mini = mini

    def __init__(self):
        self.stack = []
        
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        mini = val
        if self.stack and self.stack[-1].mini < mini:
            mini = self.stack[-1].mini
        self.stack.append(self.Pair(val,mini))

    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop().val

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1].val

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1].mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()