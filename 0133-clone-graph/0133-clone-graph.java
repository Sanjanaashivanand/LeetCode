/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if(node == null) return null;
        if(node.neighbors.isEmpty()) return new Node(node.val);

        Queue<Node> q = new LinkedList<>();
        HashMap<Node, Node> copy = new HashMap<>();

        q.offer(node);
        copy.put(node, new Node(node.val));

        while(!q.isEmpty()){
            Node curr = q.poll();

            for(Node neigh: curr.neighbors){
                if(!copy.containsKey(neigh)){
                    copy.put(neigh, new Node(neigh.val));
                    q.add(neigh);
                }
                copy.get(curr).neighbors.add(copy.get(neigh));
            }
        }

        return copy.get(node);

    }
}