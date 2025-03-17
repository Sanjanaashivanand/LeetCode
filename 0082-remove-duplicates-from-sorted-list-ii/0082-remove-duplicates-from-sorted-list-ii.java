class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode dummy = new ListNode(0); 
        dummy.next = head;
        ListNode prev = dummy; 
        ListNode temp = head;  

        while (temp != null) {
            if (temp.next != null && temp.val == temp.next.val) {
                while (temp.next != null && temp.val == temp.next.val) {
                    temp = temp.next;
                }
                prev.next = temp.next;
            } else {
                prev = prev.next; 
            }

            temp = temp.next; 
        }

        return dummy.next; 
    }
}
