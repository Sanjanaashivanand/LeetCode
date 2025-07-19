from sortedcontainers import SortedList

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        sl = SortedList()
        res = []

        for i in range(len(nums)):
            sl.add(nums[i])

            # Remove the element outside the window
            if i >= k:
                sl.remove(nums[i - k])

            if i >= k - 1:
                if k % 2 == 0:
                    median = (sl[k // 2 - 1] + sl[k // 2]) / 2.0
                else:
                    median = sl[k // 2] * 1.0
                res.append(median)

        return res