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
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null || head.next == null || k==0) return head;

        int n = 1;
        ListNode tail = head;
        while(tail.next!=null){
            n++;
            tail = tail.next;
        }

        int idx = n - (k%n);
        if(idx == 0 || idx == n) return head; 

        ListNode temp = head;
        ListNode prev = new ListNode();
        for(int i=0; i<idx; i++){
            prev = temp;
            temp = temp.next;
        }

        tail.next = head;
        prev.next = null;
        head = temp;

        return head;
    }
}