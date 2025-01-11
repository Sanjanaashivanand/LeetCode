class Solution {
    public boolean canConstruct(String s, int k) {
        if(s.length()<k) return false;

        int[] map = new int[26];

        for(char c: s.toCharArray()){
            map[c-'a']++;
        }

        int odd=0;
        int even=0;

        for(int i:map){
            if(i==0) continue;
            if(i%2==0) even++;
            else odd++;
        }

        if(odd>k) return false;

        return true;
    }
}