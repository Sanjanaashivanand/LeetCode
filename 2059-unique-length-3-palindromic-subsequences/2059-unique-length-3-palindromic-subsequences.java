class Solution {
    public int countPalindromicSubsequence(String s) {
        int[] map = new int[26];

        for(char c:s.toCharArray()){
            map[c-'a']++;
        }

        int[] L = new int[26];
        
        HashSet<Integer> S = new HashSet<>();
        for(char c: s.toCharArray()){
            map[c-'a']--;
            for(int j=0; j<26; j++){
                if(map[j]>0 && L[j]>0){
                    S.add(26*(c-'a')+j);
                }
            }
            L[c-'a']++;
        }

        return S.size();
    }
}