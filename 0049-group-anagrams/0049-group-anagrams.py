class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        frequency = {}

        for string in strs:
            count = [0] * 26

            for c in string:
                count[ord(c) - ord('a')] += 1

            count_string = ','.join(str(c) for c in count)

            if count_string not in frequency:
                frequency[count_string] = []
            frequency[count_string].append(string)

        res = []
        for i in frequency:
            res.append(frequency[i])

        return res



        