class Solution(object):
    def largestVariance(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        count = Counter(s)
        res = 0
        letters = list(set(s))

        for a in letters:
            for b in letters:
                if a == b:
                    continue

                freq_a = freq_b = 0
                remaining_b = count[b]
                has_b = False

                for ch in s:
                    if ch != a and ch != b:
                        continue

                    if ch == a:
                        freq_a += 1
                    if ch == b:
                        freq_b += 1
                        remaining_b -= 1
                        has_b = True

                    if freq_b > 0:
                        res = max(res, freq_a - freq_b)

                    if freq_b > freq_a and remaining_b > 0:
                        freq_a = freq_b = 0

        return res
