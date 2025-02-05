class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        if(s1.length()!=s2.length()) return false;
        if(s1.equals(s2)) return true;

        int counter = 0;
        int first = -1;
        int second = -1;

        for(int i=0; i<s1.length(); i++){
            if(s1.charAt(i)!=s2.charAt(i)){
                counter++;
                
                if(counter == 1){
                    first = i;
                }
                else if(counter == 2){
                    second = i;
                }
                else if(counter > 2){
                    return false;
                }
            }
        }

        return counter == 2 && s1.charAt(first) == s2.charAt(second) && s2.charAt(first) == s1.charAt(second);

    
    }
}