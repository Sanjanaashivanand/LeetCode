class Solution {
    public boolean isCircularSentence(String sentence) {
        String[] str = sentence.split(" ");

        if(str[0].charAt(0)!=str[str.length-1].charAt(str[str.length-1].length()-1)){
            return false;
        }

        for(int i=1; i<str.length; i++){
            if(str[i-1].charAt(str[i-1].length()-1) != str[i].charAt(0)){
                return false;
            }
        }

        return true;
    }
}