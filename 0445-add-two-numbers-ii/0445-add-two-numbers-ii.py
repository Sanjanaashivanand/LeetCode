# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def reverse(head):
            prev = None
            temp = head
            
            while temp!=None:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next

            return prev
        
        l1 = reverse(l1)
        l2 = reverse(l2)

        carry = 0
        dummy = ListNode(0)
        temp = dummy

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            temp.next = ListNode(total % 10)
            temp = temp.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return reverse(dummy.next)
            

        