class Solution(object):
    def pourWater(self, heights, volume, k):
        """
        :type heights: List[int]
        :type volume: int
        :type k: int
        :rtype: List[int]
        """
        n = len(heights) 
        for drop in range(0, volume):
            pour = k

            #Go left and find a dip
            for i in range(k-1, -1, -1):
                if heights[i] > heights[pour]:
                    break
                if heights[i] < heights[pour]:
                    pour = i

            if pour!=k:
                heights[pour]+=1
                continue

            #Go right
            pour = k 
            for i in range(k+1, n):
                if heights[i] > heights[pour]:
                    break
                if heights[i] < heights[pour]:
                    pour = i

            if pour!=k:
                heights[pour]+=1
                continue

            #Pour at the idx
            heights[k] += 1

        return heights


        