'''
s = "ADOBECODEBANC", t = "ABC"

t_map = {'A' : 1, 'B' : 1, 'C' : 1}
window_count = {'A': 1, 'B':1, 'C': 1}
start 
end 
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_map = Counter(t)
        start = 0
        window = defaultdict(int)

        need, have = len(t_map), 0
        res = [-1,-1]
        resLen = len(s)

        for end in range(0, len(s)):
            if s[end] in t_map:
                window[s[end]] += 1
                if window[s[end]] == t_map[s[end]]:
                    have += 1

                while have == need: #Found the string 
                    if end - start + 1 <= resLen:
                        print("Here")
                        resLen = end - start + 1
                        res = [start, end]

                    if s[start] in t_map:
                        window[s[start]] -= 1

                        if window[s[start]] < t_map[s[start]]:
                            have -= 1

                    start += 1

        return s[res[0]:res[1]+1]



                

        