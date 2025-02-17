import java.util.*;

class Solution {

    // DFS to detect cycles
    public boolean dfs(int node, ArrayList<ArrayList<Integer>> adj, boolean[] vis, boolean[] currentlyInPath) {
        // Mark the current node as visited and part of the current DFS path
        vis[node] = true;
        currentlyInPath[node] = true;

        // Explore all the neighbors
        for (int neigh : adj.get(node)) {
            if (!vis[neigh]) {
                // Recurse if the neighbor hasn't been visited yet
                if (dfs(neigh, adj, vis, currentlyInPath)) {
                    return true;  // Cycle detected
                }
            } else if (currentlyInPath[neigh]) {
                // If the neighbor is part of the current path, cycle detected
                return true;
            }
        }

        // Unmark the current node from the current DFS path
        currentlyInPath[node] = false;
        return false;
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // Step 1: Build the directed adjacency list
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }

        // Convert the prerequisites into a directed graph
        for (int[] course : prerequisites) {
            adj.get(course[1]).add(course[0]);  // course[1] -> course[0]
        }

        boolean[] vis = new boolean[numCourses];  // To mark visited nodes
        boolean[] currentlyInPath = new boolean[numCourses];  // To detect cycles during DFS

        // Step 2: Run DFS for each course
        for (int i = 0; i < numCourses; i++) {
            if (!vis[i]) {
                if (dfs(i, adj, vis, currentlyInPath)) {
                    return false;  // Cycle detected, can't finish all courses
                }
            }
        }

        return true;  // No cycle detected, all courses can be finished
    }
}
