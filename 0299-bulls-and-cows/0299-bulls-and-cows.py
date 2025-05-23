class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        s_count = {}
        g_count = {}

        # First pass: count bulls and track unmatched characters
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                s_count[secret[i]] = s_count.get(secret[i], 0) + 1
                g_count[guess[i]] = g_count.get(guess[i], 0) + 1

        # Second pass: count cows (min of remaining char frequencies)
        for ch in g_count:
            if ch in s_count:
                cows += min(s_count[ch], g_count[ch])

        return f"{bulls}A{cows}B"
