class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        for i in range(0, m + 1):  # Partition nums1 at i
            j = half - i           # Partition nums2 at j

            Aleft = nums1[i - 1] if i > 0 else float('-inf')
            Aright = nums1[i] if i < m else float('inf')

            Bleft = nums2[j - 1] if j > 0 else float('-inf')
            Bright = nums2[j] if j < n else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
                else:
                    return min(Aright, Bright)
