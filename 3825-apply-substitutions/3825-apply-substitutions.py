class Solution(object):
    def applySubstitutions(self, replacements, text):
        """
        :type replacements: List[List[str]]
        :type text: str
        :rtype: str
        """
        replaceDict = {k: v for k, v in replacements}

        #Topo Sort
        def parse(s):
            res = []
            i = 0
            while i < len(s):
                if s[i] != '%':
                    res.append(s[i])
                    i += 1

                else:
                    if '%' in replaceDict[s[i+1]]:
                        replaceDict[s[i+1]] = parse(replaceDict[s[i+1]])
                    res.append(replaceDict[s[i+1]])
                    i += 3
            return ''.join(res)

        return parse(text)


        