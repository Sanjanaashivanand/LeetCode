# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        #Find the first digit that is not nine
        temp = dummy
        while head:
            if head.val!=9:
                temp = head
            head = head.next

        temp.val += 1
        temp = temp.next

        while temp:
            temp.val = 0
            temp = temp.next

        return dummy if dummy.val else dummy.next
        