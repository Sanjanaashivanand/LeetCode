class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        res = set()
        
        def backtrack(idx, path, sumSoFar):
            if idx == n:
                return 

            if sumSoFar == target:
                res.add(tuple(path))
                return

            if sumSoFar > target:
                return

            #Pick
            backtrack(idx, path + [candidates[idx]], sumSoFar+candidates[idx])
            backtrack(idx + 1, path + [candidates[idx]], sumSoFar+candidates[idx])

            #Not Pick
            backtrack(idx + 1, path, sumSoFar)
        
        backtrack(0, [], 0)
        return list(res)