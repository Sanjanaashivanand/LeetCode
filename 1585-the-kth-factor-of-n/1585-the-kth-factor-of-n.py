class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        j = 0
        for i in range(1, n+1):
            if n%i == 0:
                j+=1
                if j == k:
                    return i
        
        return -1