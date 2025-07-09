class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        '#x#'

        encoded = ""
        for s in strs:
            delimiter = "#" + str(len(s)) + "#"
            encoded += delimiter + s

        return encoded
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        print(s)
        i = 0
        res = []
        while i<len(s):
            if s[i] == '#' and s[i+1].isdigit():
                length = 0
                j = i+1
                while s[j]!='#':
                    length = length * 10 + (int(s[j]))
                    j+=1 

                res.append(s[j+1:j+length+1])

                i = j+length

            i+=1

        return res
                       

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))