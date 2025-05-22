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
        l3 = ListNode(0)
        temp = l3

        carry = 0
        while l1!=None and l2!=None:
            if l1.val + l2.val + carry>=10:
                temp.next = ListNode((l1.val + l2.val + carry)%10)
                carry = (l1.val + l2.val + carry)//10
            else:
                temp.next = ListNode(l1.val + l2.val + carry)
                carry = 0
            temp = temp.next
            l1 = l1.next
            l2 = l2.next

        while l1!=None:
            if l1.val + carry>=10:
                temp.next = ListNode((l1.val + carry)%10)
                carry = (l1.val + carry)//10
            else:
                temp.next = ListNode(l1.val + carry)
                carry = 0
            temp = temp.next
            l1 = l1.next

        while l2!=None:
            if l2.val + carry>=10:
                temp.next = ListNode((l2.val + carry)%10)
                carry = (l2.val + carry)//10
            else:
                temp.next = ListNode(l2.val + carry)
                carry = 0
            temp = temp.next
            l2 = l2.next

        if carry!=0:
            temp.next = ListNode(carry)
            
        
        return l3.next