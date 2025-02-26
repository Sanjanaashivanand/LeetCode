import java.util.*;

class Solution {
    class DisjointSet {
        public List<Integer> rank = new ArrayList<>();
        public List<Integer> parent = new ArrayList<>();

        // Constructor to initialize the Disjoint Set
        DisjointSet(int n) {
            for (int i = 0; i < n; i++) {
                parent.add(i);
                rank.add(0);
            }
        }

        // Find with path compression
        public int findParent(int node) {
            if (node == parent.get(node)) {
                return node;
            }
            // Path compression: make the parent of the node directly point to the root
            int ulp = findParent(parent.get(node));
            parent.set(node, ulp); // Path compression
            return ulp;
        }

        // Union by rank
        public void unionByRank(int u, int v) {
            int ulp_u = findParent(u);
            int ulp_v = findParent(v);

            if (ulp_u == ulp_v) return;  // Already in the same set

            if (rank.get(ulp_u) < rank.get(ulp_v)) {
                parent.set(ulp_u, ulp_v);
            } else if (rank.get(ulp_u) > rank.get(ulp_v)) {
                parent.set(ulp_v, ulp_u);
            } else {
                parent.set(ulp_v, ulp_u);
                rank.set(ulp_u, rank.get(ulp_u) + 1);  // Increment rank
            }
        }
    }

    public int makeConnected(int n, int[][] connections) {
        // If there are fewer connections than n-1, return -1 as it's impossible to connect all nodes
        if (connections.length < n - 1) {
            return -1;
        }

        // Initialize the Disjoint Set
        DisjointSet ds = new DisjointSet(n);

        // Count extra edges that don't help in connecting new components
        int cntExtras = 0;
        for (int[] edge : connections) {
            int u = edge[0];
            int v = edge[1];
            if (ds.findParent(u) == ds.findParent(v)) {
                cntExtras++;  // Extra edge, no new component is formed
            } else {
                ds.unionByRank(u, v);  // Union the sets
            }
        }

        // Count the number of components
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (ds.findParent(i) == i) {
                cnt++;  // Count the number of disjoint sets
            }
        }

        // The answer is the number of components minus 1, as we need n-1 edges to connect n components
        int ans = cnt - 1;

        // If we have enough extra edges to form the MST, return the answer
        if (cntExtras >= ans) {
            return ans;
        }

        return -1;  // Not enough extra edges to form a connected network
    }
}
