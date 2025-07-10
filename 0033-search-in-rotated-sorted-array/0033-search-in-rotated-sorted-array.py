class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        low = 0
        high = n-1

        while low <= high:
            mid = (low+high)//2

            if nums[mid] == target:
                return mid

            #Mid is in left portion
            if nums[mid] >= nums[low]:
                #target is in the left portion
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            #Mid is in right portion
            else:
                #target is in the right portion
                if nums[mid] <= target <= nums[high]:
                    low = mid+1
                else:
                    high = mid - 1

        return -1