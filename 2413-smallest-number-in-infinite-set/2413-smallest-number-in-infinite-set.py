class SmallestInfiniteSet(object):

    def __init__(self):
        self.added_integers = []
        self.is_present = set()
        self.curr = 1

    def popSmallest(self):
        """
        :rtype: int
        """
        if len(self.added_integers):
            ans = heappop(self.added_integers)
            self.is_present.remove(ans)
        else:
            ans = self.curr
            self.curr += 1
        return ans

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.curr <= num or num in self.is_present:
            return
        heappush(self.added_integers, num)
        self.is_present.add(num)


        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)