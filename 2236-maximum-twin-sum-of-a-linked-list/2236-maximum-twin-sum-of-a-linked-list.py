
from sys import maxsize# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        curr = head
        s = []
        max_sum = 0

        while curr:
            s.append(curr.val)
            curr = curr.next
        
        n = len(s)
        for i in range(0, n//2):
            max_sum = max(max_sum, s[i] + s.pop())
        
        return max_sum
