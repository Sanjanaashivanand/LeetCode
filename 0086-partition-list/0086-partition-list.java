/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode lessNode = new ListNode(0);
        ListNode greaterNode = new ListNode(0);
        ListNode ptr1 = lessNode;
        ListNode ptr2 = greaterNode;

        while (head != null) {
            if (head.val < x) {
                ptr1.next = new ListNode(head.val);
                ptr1 = ptr1.next;
            } else {
                ptr2.next = new ListNode(head.val);
                ptr2 = ptr2.next;
            }
            head = head.next;
        }
        ptr1.next = greaterNode.next;
        ptr2.next = null;
        return lessNode.next;

    }
}