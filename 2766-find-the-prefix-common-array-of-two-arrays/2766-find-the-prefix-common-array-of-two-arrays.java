class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int[] res = new int[A.length];
        int[] count = new int[A.length+1];
        int common = 0;

        for(int i=0; i<A.length; i++){
            count[A[i]]++;
            if(count[A[i]]==2) common++;
            count[B[i]]++;
            if(count[B[i]]==2) common++;
            res[i] = common;
        }
        
        return res;
    }
}