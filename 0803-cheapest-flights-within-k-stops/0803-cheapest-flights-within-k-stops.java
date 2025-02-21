import java.util.*;

class Solution {
    class Pair {
        int node;
        int cost;
        int layover;

        Pair(int node, int cost, int layover) {
            this.node = node;
            this.cost = cost;
            this.layover = layover;
        }
    }

    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        // Create adjacency list to represent the graph
        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        // Build the graph from the flight information
        for (int[] flight : flights) {
            adj.get(flight[0]).add(new Pair(flight[1], flight[2], 0));  // Add destination and cost
        }

        // Distance array to track the minimum cost to each node
        int[] dis = new int[n];
        Arrays.fill(dis, Integer.MAX_VALUE);
        dis[src] = 0;

        // Priority queue to store nodes (cost, node, layovers)
        Queue<Pair> pq = new LinkedList<>();
        pq.offer(new Pair(src, 0, 0));  // Start from the source with 0 cost and 0 layovers

        while (!pq.isEmpty()) {
            Pair curr = pq.poll();
            int currSrc = curr.node;
            int cost = curr.cost;
            int layovers = curr.layover;

            // If we exceed the maximum allowed layovers, skip further exploration
            if (layovers > k) continue;

            // Explore all neighbors (destination cities)
            for (Pair destination : adj.get(currSrc)) {
                int nextNode = destination.node;
                int nextCost = cost + destination.cost;

                // Only explore the path if it leads to a cheaper cost and  fewer layovers
                if (nextCost < dis[nextNode] && layovers + 1 < dis[nextNode]) {
                    dis[nextNode] = nextCost;
                    pq.offer(new Pair(nextNode, nextCost, layovers + 1));
                }
            }
        }

       
        return dis[dst] == Integer.MAX_VALUE ? -1 : dis[dst];
    }
}
