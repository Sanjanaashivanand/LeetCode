class Solution:
    #Empty
    #1, 2, 3 .... 9
    #123 123 123 

    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def recurse(i):
            if i > n:
                return
            res.append(i)
            for j in range(10):
                if i * 10 + j > n:
                    break
                recurse(i * 10 + j)

        for i in range(1, 10):
            recurse(i)

        return res


        
