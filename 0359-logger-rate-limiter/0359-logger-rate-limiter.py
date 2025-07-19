class Logger(object):

    def __init__(self):
        self.traffic = {}
        self.q = deque()
        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        while self.q and timestamp - self.q[0][0] >= 10:
            old_time, old_message = self.q.popleft()
            if self.traffic[old_message] == old_time:
                del self.traffic[old_message]

        if message not in self.traffic:
            self.traffic[message] = timestamp
            self.q.append((timestamp, message))
            return True

        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)