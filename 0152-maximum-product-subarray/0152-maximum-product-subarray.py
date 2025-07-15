class Solution(object):
    def maxProduct(self, nums):
        max_prod = 1
        min_prod = 1

        res = nums[0]

        for num in nums:
            if num == 0:
                max_prod = 1
                min_prod = 1
                res = max(res, 0)
                continue

            temp = max_prod
            max_prod = max(max_prod*num, min_prod*num, num)
            min_prod = min(min_prod*num, temp*num, num)

            res = max(max_prod, res)

        return res