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
        res = ListNode(0)
        temp3 = res

        temp1 = l1
        temp2 = l2

        carry = 0
        while temp1 and temp2:
            if temp1.val + temp2.val + carry >= 10:
                temp3.next = ListNode((temp1.val + temp2.val + carry)%10)
                carry = 1
            else:
                temp3.next = ListNode(temp1.val + temp2.val + carry)
                carry = 0

            temp1 = temp1.next
            temp2 = temp2.next
            temp3 = temp3.next

        while temp1:
            sum_val = temp1.val + carry
            temp3.next = ListNode(sum_val % 10)
            carry = sum_val // 10

            temp1 = temp1.next
            temp3 = temp3.next


        while temp2:
            sum_val = temp2.val + carry
            temp3.next = ListNode(sum_val % 10)
            carry = sum_val // 10

            temp2 = temp2.next
            temp3 = temp3.next

        if carry !=0:
            temp3.next = ListNode(carry)

        return res.next

