class MyHashMap {
    class Node {
        int idx;
        int val;
        Node next;

        Node(int idx, int val) {
            this.idx = idx;
            this.val = val;
        }
    }

    Node head;

    public MyHashMap() {
        this.head = new Node(-1, -1); // dummy head
    }

    public void put(int key, int value) {
        Node temp = head;

        // If key already exists, update it
        while (temp.next != null) {
            if (temp.next.idx == key) {
                temp.next.val = value;
                return;
            }
            temp = temp.next;
        }

        // Else add new node at the end
        temp.next = new Node(key, value);
    }

    public int get(int key) {
        Node temp = head.next; // skip dummy node
        while (temp != null) {
            if (temp.idx == key) {
                return temp.val;
            }
            temp = temp.next;
        }
        return -1;
    }

    public void remove(int key) {
        Node prev = head;
        Node temp = head.next;

        while (temp != null) {
            if (temp.idx == key) {
                prev.next = temp.next; // skip the node to be deleted
                return;
            }
            prev = temp;
            temp = temp.next;
        }
    }
}
