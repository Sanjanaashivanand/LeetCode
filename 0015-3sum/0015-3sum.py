class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []

        for curr in range(0, n):
            low = curr+1
            high = n-1

            if curr > 0 and nums[curr-1] == nums[curr]:
                continue
            

            while low<high:
                if nums[low] + nums[high] + nums[curr] == 0:
                    res.append([nums[curr], nums[low] , nums[high]])
                    while low < high and nums[low+1] == nums[low]:
                        low+=1
                    while low<high and nums[high-1] == nums[high]:
                        high-=1

                if nums[low] + nums[high] > (-1) * nums[curr]:
                    high -= 1
                else:
                    low += 1


        return res
