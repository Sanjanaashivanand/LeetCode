class MyLinkedList {
    class Node {
        int val;
        Node next;

        Node(int val) {
            this.val = val;
        }
    }

    Node head;
    int len;

    public MyLinkedList() {
        this.head = null;
        this.len = 0;
    }

    public int get(int index) {
        if (head == null || index >= len) return -1;

        Node temp = head;
        for (int i = 0; i < index; i++) {
            temp = temp.next;
        }

        return temp == null ? -1 : temp.val;
    }

    public void addAtHead(int val) {
        Node newNode = new Node(val);
        newNode.next = head;
        head = newNode;
        len++;
    }

    public void addAtTail(int val) {
        if (head == null) {
            addAtHead(val);
            return;
        }

        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }

        temp.next = new Node(val);
        len++;
    }

    public void addAtIndex(int index, int val) {
        if (index > len) return;

        if (index == 0) {
            addAtHead(val);
            return;
        }

        if (index == len) {
            addAtTail(val);
            return;
        }

        Node prev = null;
        Node temp = head;

        for (int i = 0; i < index; i++) {
            prev = temp;
            temp = temp.next;
        }

        Node newNode = new Node(val);
        prev.next = newNode;
        newNode.next = temp;
        len++;
    }

    public void deleteAtIndex(int index) {
        if (index >= len || head == null) return;

        if (index == 0) {
            head = head.next;
            len--;
            return;
        }

        Node prev = null;
        Node temp = head;

        for (int i = 0; i < index; i++) {
            prev = temp;
            temp = temp.next;
        }

        if (temp != null) {
            prev.next = temp.next;
            temp.next = null;
        } else {
            prev.next = null;
        }

        len--;
    }
}
