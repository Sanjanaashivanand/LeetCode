class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])  # sort by end time
    
        curr_end = float('-inf')
        count = 0

        for pair in pairs:
            if pair[0] > curr_end:
                count += 1
                curr_end = pair[1]

        return count
        