class Solution:
    #10 -> 1,2,3,4,5,6,7,8,9, 10 => 2
    #100 -> 1,10, 100, 11,12,13,14,15,16,17,18,19 => 12
    #1000 -> 1,10,100, 1000, 11, 110, .... -> x => 112

    
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k-=1

        def count_steps(prefix1, prefix2):
            steps = 0
            while prefix1 <= n:
                steps += min(n + 1, prefix2) - prefix1
                prefix1 *= 10
                prefix2 *= 10
            return steps

        while k > 0:
            step = count_steps(curr, curr + 1)
            if step <= k:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1
        
        return curr