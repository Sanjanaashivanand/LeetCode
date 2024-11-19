class Solution {
    public int[] decrypt(int[] code, int k) {
        int[] res = new int[code.length];

        for(int i=0; i<code.length; i++){
            if(k>0){
                for(int j=i+1; j<i+1+k; j++){
                    res[i] += code[j % code.length];
                }
            }
            else if(k<0){
                for(int j=i-1; j>i-1-Math.abs(k); j--){
                    res[i] += code[((j % code.length) + code.length)%code.length];
                }
            }
        }

        return res;
    }
}