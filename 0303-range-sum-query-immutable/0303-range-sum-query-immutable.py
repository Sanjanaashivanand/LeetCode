'''
[-2, 0, 3, -5, 2, -1]
[-2, -2, 1, -4, -2, -3]
'''
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = []
        self.prefix.append(0)

        for i in range(0, len(nums)):
            self.prefix.append(self.prefix[-1]+nums[i])

        print(self.prefix)

        
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        res = self.prefix[right+1] - self.prefix[left]
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)