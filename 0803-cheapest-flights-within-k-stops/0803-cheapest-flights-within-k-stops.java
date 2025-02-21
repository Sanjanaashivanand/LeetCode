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

    class Dist {
        int dis;
        int layovers;

        Dist(int dis, int layovers) {
            this.dis = dis;
            this.layovers = layovers;
        }
    }

    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        if (src == dst) {
            return 0;  // No flight needed if source and destination are the same
        }

        // Adjacency list to store the graph
        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        // Build the graph
        for (int[] flight : flights) {
            adj.get(flight[0]).add(new Pair(flight[1], flight[2], 0)); // Add flight with cost and layover
        }

        // Distance array to store the shortest path cost and number of layovers
        Dist[] dis = new Dist[n];
        for (int i = 0; i < n; i++) {
            dis[i] = new Dist(Integer.MAX_VALUE, Integer.MAX_VALUE);
        }

        // Min-heap priority queue to process nodes in increasing order of cost
        PriorityQueue<Pair> pq = new PriorityQueue<>((x, y) -> x.layover - y.layover);

        // Start from the source node (src)
        dis[src].dis = 0;
        dis[src].layovers = 0;
        pq.add(new Pair(src, 0, 0));

        while (!pq.isEmpty()) {
            Pair curr = pq.poll();
            int r = curr.node;
            int cost = curr.cost;
            int layovers = curr.layover;

            // Skip if we've already processed a node with fewer or equal layovers
            if (layovers > k) continue;

            // Explore all neighboring nodes (destinations)
            for (Pair destination : adj.get(r)) {
                int nextNode = destination.node;
                int nextCost = cost + destination.cost;

                // If we find a cheaper cost to reach nextNode with fewer layovers, update it
                if (nextCost < dis[nextNode].dis || (nextCost == dis[nextNode].dis && layovers + 1 < dis[nextNode].layovers)) {
                    dis[nextNode].dis = nextCost;
                    dis[nextNode].layovers = layovers + 1;
                    pq.offer(new Pair(nextNode, nextCost, layovers + 1));
                }
            }
        }

        // If the destination is unreachable or has exceeded the allowed layovers, return -1
        return dis[dst].dis == Integer.MAX_VALUE ? -1 : dis[dst].dis;
    }
}
