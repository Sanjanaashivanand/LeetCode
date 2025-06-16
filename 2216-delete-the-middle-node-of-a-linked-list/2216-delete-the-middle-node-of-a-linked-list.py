# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Input: Head of a linked list
Output: Head of a linked list => in place

1. Traves and calculate n
2. travese again and remove the middle node

'''
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next or not head:
            return head.next

        temp = head
        n = 0
        while temp:
            n+=1
            temp = temp.next

        mid = n//2
        prev = head
        temp = head
        k = 0

        while k<=mid:
            if k==mid:
                prev.next = temp.next
                temp.next = None
                break
            
            prev = temp 
            temp = temp.next
            k+=1
        
        return head

        
        