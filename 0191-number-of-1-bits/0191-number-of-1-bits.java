class Solution {
    public int hammingWeight(int n) {
        String binary = Integer.toBinaryString(n);

        int res = 0;
        for(char c : binary.toCharArray()){
            if(c == '1'){
                res++;
            }
        }

        return res;
    }
}