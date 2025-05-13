class Solution(object):
    def isMonotonic(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
       

        inc = dec = True

        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                dec = False
            if arr[i]>arr[i+1]:
                inc = False
        
        return dec or inc