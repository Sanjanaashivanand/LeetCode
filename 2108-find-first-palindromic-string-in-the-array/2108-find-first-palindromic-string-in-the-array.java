class Solution {
    public boolean isPalindrome(String s){
        int n = s.length();
        for(int i=0; i<(int)n/2;i++){
            if(s.charAt(i)!=s.charAt(n-i-1)){
                return false;
            }
        }

        return true;
    }
    public String firstPalindrome(String[] words) {
        for(String s : words){
            if(isPalindrome(s)){
                return s;
            }
        }

        return "";
        
    }
}