class Solution {
    public boolean checkString(String s) {
        int countA = 0;
        int countB = 0;

        for(char c : s.toCharArray()){
            if(c == 'a'){
                countA++;
            }
        }

        for(char c : s.toCharArray()){
            if(c == 'a'){
                countA--;
            }
            else{
                countB++;
            }

            if(countA!=0 && countB>0) return false;
        }

        return true;
    }
}