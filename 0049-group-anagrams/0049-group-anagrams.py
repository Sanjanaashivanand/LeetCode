class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        freq_map = {}

        for s in strs:
            char_map = [0] * 26
            for c in s:
                char_map[ord(c)-ord('a')] += 1

            key = ','.join(str(i) for i in char_map)
            if key not in freq_map:
                freq_map[key] = []
            freq_map[key].append(s)
        
        res = []
        for val in freq_map.values():
            res.append(val)

        return res

                