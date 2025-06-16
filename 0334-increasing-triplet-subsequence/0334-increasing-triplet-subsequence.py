'''
In: Array of integers (pos and neg)
Ou: boolean (true, false)

To Do:  check is there is a triplet such that 3 consecutive numbers are in increasing order

[0,4,2,1,0,-1,-3]

Idea: to retain the smallest elements in the queue
f = 20 s = 100

10: f = 10


'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = float('inf')
        s = float('inf')

        for i in range(0, len(nums)):
            if nums[i] <= f:
                f = nums[i]
            elif nums[i] <= s:
                s = nums[i]
            else:
                return True
        
        return False

