import java.util.*;

class Solution {
    class Pair {
        int node;
        long time;

        Pair(int node, long time) {
            this.node = node;
            this.time = time;
        }
    }

    public int countPaths(int n, int[][] roads) {
        // Create adjacency list for the graph
        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] road : roads) {
            adj.get(road[0]).add(new Pair(road[1], road[2]));
            adj.get(road[1]).add(new Pair(road[0], road[2]));  
        }

        int mod = 1000000007;
        long[] dis = new long[n];
        Arrays.fill(dis, Long.MAX_VALUE);
        dis[0] = 0;

        // Ways array to store the number of shortest paths to each node
        int[] ways = new int[n];
        Arrays.fill(ways, 0);
        ways[0] = 1;  // There's 1 way to be at the source node (starting point)

        // Min-heap priority queue to store nodes (time, node)
        PriorityQueue<Pair> pq = new PriorityQueue<>((x, y) -> Long.compare(x.time, y.time));
        pq.offer(new Pair(0, 0));  // Start from node 0 with 0 time

        // Dijkstra's algorithm to find the shortest path and count the number of ways
        while (!pq.isEmpty()) {
            Pair curr = pq.poll();
            int currNode = curr.node;
            long currTime = curr.time;

            // Explore all neighboring nodes (destinations)
            for (Pair next : adj.get(currNode)) {
                int nextNode = next.node;
                long nextTime = next.time;

                // If a shorter path to nextNode is found
                if (currTime + nextTime < dis[nextNode]) {
                    dis[nextNode] = currTime + nextTime;
                    ways[nextNode] = ways[currNode]; // Set the number of ways to reach nextNode
                    pq.offer(new Pair(nextNode, dis[nextNode]));
                }
                // If another shortest path to nextNode is found
                else if (currTime + nextTime == dis[nextNode]) {
                    ways[nextNode] = (ways[nextNode] + ways[currNode]) % 1000000007;
                }
            }
        }

        // Return the number of ways to reach the destination node (node n-1)
        return ways[n - 1];
    }
}
