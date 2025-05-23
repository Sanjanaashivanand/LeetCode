class MyCircularQueue {
    class Node{
        int val;
        Node next;

        Node(int val){
            this.val = val;
        }
    }

    Node head;
    Node tail;
    int max;
    int len;

    public MyCircularQueue(int k) {
        this.head = null;
        this.tail = null;
        this.max = k;
        this.len = 0;
    }
    
    public boolean enQueue(int value) {
        if(len>=max) return false;

        Node newNode = new Node(value);
        this.len++;

        if(this.head==null && this.tail==null){
            this.head = newNode;
            this.tail = newNode;
            return true;
        }

        tail.next = newNode;
        tail = newNode;
        return true;
    }
    
    public boolean deQueue() {
        if(len == 0) return false;

        this.len--;
        if(head == tail){
            this.head = null;
            this.tail = null;
            return true;
        }

        this.head = this.head.next;
        return true;
    }
    
    public int Front() {
        if(head==null) return -1;
        return head.val;
    }
    
    public int Rear() {
        if(tail==null) return -1;
        return tail.val;
    }
    
    public boolean isEmpty() {
        return this.len == 0;
    }
    
    public boolean isFull() {
        return this.len == this.max;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */