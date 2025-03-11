class Solution {
    public int numberOfSubstrings(String s) {
        int[] count = new int[3];
        int i = 0, j = 0;
        int res = 0;

        while(j < s.length()){
            char right = s.charAt(j);
            count[right - 'a']++;

            while (count[0] > 0 && count[1] > 0 && count[2] > 0) {
                res += s.length() - j;
                count[s.charAt(i) - 'a']--;
                i++;
            }

            j++;
        }

        return res;
    }
}