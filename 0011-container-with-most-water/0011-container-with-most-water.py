'''
height = [1,8,6,2,5,4,8,3,7]


'''


class Solution(object):
    def maxArea(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        max_area = -1

        while l<r:
            area = (r-l) * min(nums[r], nums[l])
            max_area = max(max_area, area)
            if nums[l] < nums[r]:
                l+=1
            else:
                r-=1

        return max_area

        


        