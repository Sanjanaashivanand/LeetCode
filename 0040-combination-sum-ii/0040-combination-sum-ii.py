class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(list(path))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # skip duplicates

                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res
