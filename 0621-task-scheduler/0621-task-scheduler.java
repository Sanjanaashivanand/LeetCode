class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] count = new int[26];
        for(char c:tasks){
            count[c-'A']++;
        }
        Arrays.sort(count);
        int max_val = count[25] - 1;
        int ideal_slots = max_val * n;

        for(int i=24; i>=0; i--){
            ideal_slots -= Math.min(count[i], max_val);
        }

        return ideal_slots > 0 ? ideal_slots + tasks.length : tasks.length;



    }
}