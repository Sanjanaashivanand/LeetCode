class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        res = 0

        while i < len(chars):
            curr = chars[i]
            count = 0

            while i < len(chars) and chars[i] == curr:
                i += 1
                count += 1
            
            chars[res] = curr
            res+=1

            if count > 1:
                for c in str(count):
                    chars[res] = c
                    res += 1
        
        return res
                



        