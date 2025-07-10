
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n-1
        res = nums[0]

        while low<=high:
            if nums[low] < nums[high]:
                res = min(res, nums[low])
                break

            mid = (low+high)//2
            res = min(res, nums[mid])
            
            #Mid is in left portion
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1

        return res




            
       