# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        start = head

        while start:
            end = start
            # Check if there are k nodes to reverse
            for i in range(k - 1):
                end = end.next
                if not end:
                    return dummy.next

            next_group_start = end.next

            # Reverse from start to end
            prev = None
            curr = start
            while curr != next_group_start:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # Connect with the previous part
            prev_group_end.next = end
            start.next = next_group_start  # start is now the end of the reversed group
            prev_group_end = start  # move prev_group_end for next group
            start = next_group_start  # move start for next group

        return dummy.next
