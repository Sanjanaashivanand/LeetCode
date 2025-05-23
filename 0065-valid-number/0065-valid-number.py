class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        num_seen = dot_seen = e_seen = False
        num_after_e = True  # Must be True by default if no 'e' is seen

        for i, char in enumerate(s):
            if char.isdigit():
                num_seen = True
                if e_seen:
                    num_after_e = True
            elif char in ['+', '-']:
                if i != 0 and s[i - 1].lower() != 'e':
                    return False
            elif char == '.':
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            elif char.lower() == 'e':
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_after_e = False
            else:
                return False

        return num_seen and num_after_e
