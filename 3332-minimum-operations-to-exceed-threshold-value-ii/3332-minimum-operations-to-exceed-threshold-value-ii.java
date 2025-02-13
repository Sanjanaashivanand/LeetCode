class Solution {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Long> q = new PriorityQueue<>();

        for(int i: nums){
            q.add(new Long(i));
        }

        int res = 0;

        while(q.peek()<k){
            long a = q.poll();
            long b = q.poll();
            q.add(Math.min(a, b) * 2 + Math.max(a,b));
            res++;
        }

        return res;
    }
}