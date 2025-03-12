class Solution {
    public boolean areNumbersAscending(String string) {
        int prev = -1;
        String[] strs = string.split(" ");

        for(String s : strs){
            if(!Character.isDigit(s.charAt(0))) continue;

            int num = 0;
            for(char c : s.toCharArray()){
                num = num * 10 + (c - '0');
            }

            if(prev >= num) return false;

            prev = num;
        }

        return true;
    }
}