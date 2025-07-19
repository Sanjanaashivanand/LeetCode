class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        maps = {}
        seen = set()

        words = s.split(" ")

        if len(words)!=len(pattern):
            return False

        for word, letter in zip(words, pattern):
            if letter not in maps:
                if word not in seen:
                    maps[letter] = word
                    seen.add(word)
                else:
                    return False
            else:
                if maps[letter] != word:
                    return False

        return True