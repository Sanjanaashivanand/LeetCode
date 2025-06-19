class Solution(object):
    def backtrack(self, digitToString, digits, i, s):
        if i == len(digits):
            self.res.append(s)
            return

        digit = int(digits[i])

        for c in digitToString[digit]:
            s+=c
            self.backtrack(digitToString, digits, i+1, s)
            s = s[:-1]

        

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) == 0:
            return []

        digitToString = {
            2 : "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }   

        self.res = []
        self.backtrack(digitToString, digits, 0, "")
        return self.res


        