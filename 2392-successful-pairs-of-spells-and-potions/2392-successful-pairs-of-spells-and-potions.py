class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        res = []
        potions.sort()
        n = len(potions)
        max_potion = potions[n-1]

        for spell in spells:
            min_potion = (success + spell -1) // spell

            if min_potion > max_potion:
                res.append(0)
                continue

            low = 0
            high = n-1

            while low < high:
                mid = (low+high)//2

                if potions[mid] < min_potion:
                    low = mid+1
                else:
                    high = mid

            res.append(n-low)

        return res
            
