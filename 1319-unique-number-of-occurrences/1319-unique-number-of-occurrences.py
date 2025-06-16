class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = {}
        for i in arr:
            if i not in count:
                count[i] = 0
            count[i] += 1

        uni = set()
        for i in count.values():
            if i in uni:
                return False
            uni.add(i)
        return True