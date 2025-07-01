class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = {}  # key: index, value: (length, count)
        lenLIS, res = 0, 0

        for i in range(n - 1, -1, -1):
            maxLen, maxCnt = 1, 1  # default for each index

            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    currLen, currCnt = dp[j]
                    if currLen + 1 > maxLen:
                        maxLen = currLen + 1
                        maxCnt = currCnt
                    elif currLen + 1 == maxLen:
                        maxCnt += currCnt

            dp[i] = (maxLen, maxCnt)

            if maxLen > lenLIS:
                lenLIS = maxLen
                res = maxCnt
            elif maxLen == lenLIS:
                res += maxCnt

        return res