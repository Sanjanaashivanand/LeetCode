class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        Queue<Integer> q = new LinkedList<>();

        for(int i=0; i<intervals.length; i++){
            if(newInterval[1] < intervals[i][0]){
                q.offer(newInterval[0]);
                q.offer(newInterval[1]);

                for(int j=i; j<intervals.length; j++){
                    q.offer(intervals[j][0]);
                    q.offer(intervals[j][1]);
                }
                
                System.out.println(q);
                int[][] res = new int[q.size()/2][2];
                int k = 0;

                while(!q.isEmpty()){
                    res[k][0] = q.poll();
                    res[k++][1] = q.poll();
                }

                return res;
            }
            else if(newInterval[0] > intervals[i][1]){
                q.offer(intervals[i][0]);
                q.offer(intervals[i][1]);
            }
            else{
                newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
                newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            }
        }

        q.offer(newInterval[0]);
        q.offer(newInterval[1]);

        int[][] res = new int[q.size()/2][2];
        int k = 0;
        while(!q.isEmpty()){
            res[k][0] = q.poll();
            res[k++][1] = q.poll();
        }

        return res;
    }
}
