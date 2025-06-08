class Solution:
    #Input: Integer (positive)
    #Output: Array from 1 to n sorted lexicalOrder]


    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1, n+1):
            res.append(str(i))
        res.sort()

        dig = []
        for i in range(0, n):
            dig.append(int(res[i]))
        return dig