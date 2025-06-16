# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        prev_odd = None 
        prev_even = None
        even_head = even

        while even and even.next:
            prev_odd = odd
            odd = even.next 

            prev_even = even
            even = odd.next

            prev_odd.next = odd
            prev_even.next = even

        odd.next = even_head

        return head

        