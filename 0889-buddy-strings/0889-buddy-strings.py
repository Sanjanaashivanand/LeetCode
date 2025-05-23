class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False

        if s == goal:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')]+=1
                if freq[ord(ch) - ord('a')] == 2:
                    return True
            return False

        count = 0
        mismatch = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                count += 1
                if count > 2:
                    return False
                mismatch.append((s[i], goal[i]))

        if count != 2:
            return False

        return mismatch[0] == mismatch[1][::-1]
