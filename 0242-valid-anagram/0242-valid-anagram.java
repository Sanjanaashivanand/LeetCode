class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()) return false;

        int[] map = new int[26];

        for(int i=0; i<s.length(); i++){
            map[(int)s.charAt(i) - 'a']++;
            map[(int)t.charAt(i) - 'a']--;
        }

        for(int i:map){
            if(i!=0){
                return false;
            }
        }

        return true;

    }
}