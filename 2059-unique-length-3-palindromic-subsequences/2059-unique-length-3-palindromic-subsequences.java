class Solution {
    public int countPalindromicSubsequence(String s) {
        int[] right = new int[26];
        for(char c : s.toCharArray()){
            right[c-'a']++;
        }

        int[] left = new int[26];

        HashSet<Integer> set = new HashSet<>();

        for(char c : s.toCharArray()){
            right[c-'a']--;
            for(int i=0; i<26; i++){
                if(right[i]>0 && left[i]>0){
                    set.add(26*(c-'a') + i);
                }
            }
            left[c-'a']++;
        }

        return set.size();
    }
}