class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        freq_map = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key not in freq_map:
                freq_map[key] = []
            freq_map[key].append(s)
        
        res = []
        for val in freq_map.values():
            res.append(val)

        return res

                