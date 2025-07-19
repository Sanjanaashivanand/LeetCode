class Logger(object):

    def __init__(self):
        self.traffic = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.traffic:
            self.traffic[message] = timestamp  
            return True

        prev = self.traffic[message]
        if timestamp - prev >= 10:
            self.traffic[message] = timestamp
            return True

        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)