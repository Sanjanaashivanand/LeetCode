
class Solution(object):

    def backtrack(self, nums, curr_sum, start, k, n):
        if len(nums) == k:
            if curr_sum == n:
                self.res.append(list(nums))
            return
        
        if curr_sum > n or len(nums)>k:
            return

        for i in range(start+1, 10):
            if curr_sum + i > n:
                break

            if i not in nums:
                nums.add(i)
                curr_sum+=i 
                self.backtrack(nums, curr_sum, i, k, n)
                nums.discard(i)
                curr_sum-=i 
        

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        for i in range(1,10):
            nums = set()
            nums.add(i)
            self.backtrack(nums, i, i, k, n)

        return self.res
        


            

            