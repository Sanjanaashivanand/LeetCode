# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        def mergeList(list1, list2):
            dummy = ListNode(0)
            temp = dummy
            
            while list1 and list2:
                if list1.val < list2.val:
                    temp.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    temp.next = ListNode(list2.val)
                    list2 = list2.next
                temp=temp.next

            if list1:
                temp.next = list1
            if list2:
                temp.next = list2

            return dummy.next
        
        if not lists: 
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                merged.append(mergeList(l1, l2))
            lists = merged

        return lists[0]

        return res


