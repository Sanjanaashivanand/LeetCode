class Solution {
    public int lengthAfterTransformations(String s, int t) {
        int[] count = new int[26];
        int MOD = 1000000007;

        for(char c : s.toCharArray()){
            count[c - 'a']++;
        }

        for(int times=0; times<t; times++){
            int[] next = new int[26];

            next[0] = count[25];
            next[1] = (count[25] + count[0]) % MOD;
            for(int i=2; i<26; i++){
                next[i] = count[i-1];
            }
            count = next;
        }

        int ans = 0;
        for(int i:count){
            ans = (ans + i) % MOD;
        }

        return ans;
    }
}