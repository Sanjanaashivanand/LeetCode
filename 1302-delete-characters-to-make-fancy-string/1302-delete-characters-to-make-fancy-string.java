class Solution {
    public String makeFancyString(String s) {
        StringBuilder res = new StringBuilder();
        int count = 1; // Start count at 1 for the first character
        res.append(s.charAt(0));
        
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                count++;
            } else {
                count = 1; // Reset count for a new character
            }
            
            if (count <= 2) {
                res.append(s.charAt(i));
            }
        }
        
        return res.toString();
    }
}
