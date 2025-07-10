class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)

        total = m + n
        half = total // 2

        l = 0
        r = len(nums1) - 1

        while True:
            i = (l+r)//2
            j = half - i - 2

            Aleft = nums1[i] if i>= 0 else float('-inf')
            Aright = nums1[i+1] if i+1<m else float('inf')

            Bleft = nums2[j] if j>=0 else float('-inf')
            Bright = nums2[j+1] if j+1<n else float('inf')

            if Aleft<=Bright and Bleft<=Aright:
                if total%2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
                return min(Aright, Bright)

            elif Aleft > Bright:
                r = i - 1
            else: 
                l = i + 1