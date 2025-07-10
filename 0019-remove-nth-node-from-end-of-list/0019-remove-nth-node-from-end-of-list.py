# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        right = head

        while n!=0:
            right = right.next
            n -= 1

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        left = head

        while right:
            prev = left
            left = left.next
            right = right.next

        prev.next = left.next
        return dummy.next


        