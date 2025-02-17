class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for(int i=0; i<numCourses; i++){
            adj.add(new ArrayList<>());
        }

        for(int[] prereq: prerequisites){
            adj.get(prereq[1]).add(prereq[0]);
        }

        int[] indegree = new int[numCourses];

        for(ArrayList<Integer> adjacent: adj){
            for(int i: adjacent){
                indegree[i]++;
            }
        }

        Queue<Integer> q = new LinkedList<>();

        for(int i=0; i<numCourses; i++){
            if(indegree[i]==0){
                q.add(i);
            }
        }

        ArrayList<Integer> res = new ArrayList<>();

        while(!q.isEmpty()){
            int node = q.poll();
            res.add(node);

            for(int neigh: adj.get(node)){
                indegree[neigh]--;
                if(indegree[neigh]==0){
                    q.add(neigh);
                }
            }
        }

        if(res.size()!=numCourses){
            return new int[0];
        }

        int[] result = new int[numCourses];

        for(int i=0; i<numCourses; i++){
            result[i] = res.get(i);
        }

        return result;
    }
}