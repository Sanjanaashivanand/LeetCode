class BrowserHistory {
    class Node {
        String homepage;
        Node next;
        Node prev;

        Node(String homepage) {
            this.homepage = homepage;
        }
    }

    Node curr;

    public BrowserHistory(String homepage) {
        curr = new Node(homepage);
    }

    public void visit(String url) {
        Node newNode = new Node(url);
        curr.next = null;  // Cut off forward history
        newNode.prev = curr;
        curr.next = newNode;
        curr = newNode;
    }

    public String back(int steps) {
        while (steps-- > 0 && curr.prev != null) {
            curr = curr.prev;
        }
        return curr.homepage;
    }

    public String forward(int steps) {
        while (steps-- > 0 && curr.next != null) {
            curr = curr.next;
        }
        return curr.homepage;
    }
}
