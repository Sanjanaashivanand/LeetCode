class Solution {
    public boolean closeStrings(String word1, String word2) {
        if(word1.length()!=word2.length()) return false;
        
        int[] w1map = new int[26];
        int[] w2map = new int[26];

        for(int i=0; i<word1.length(); i++){
            w1map[(int)word1.charAt(i)-97]++;
            w2map[(int)word2.charAt(i)-97]++;
        }

        for (int i = 0; i < 26; i++) {
            if (w1map[i] == w2map[i]) {
                continue;
            }
            if (w1map[i] == 0 || w2map[i] == 0) {
                return false;
            }
        }
        Arrays.sort(w1map);
        Arrays.sort(w2map);
        for (int i = 0; i < 26; i++) {
            if (w1map[i] != w2map[i]) {
                return false;
            }
        }
        return true;
        
        
    }
}