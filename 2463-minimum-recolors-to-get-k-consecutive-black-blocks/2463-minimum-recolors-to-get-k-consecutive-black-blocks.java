class Solution {
    public int minimumRecolors(String blocks, int k) {
        int i = 0;
        int cw = 0;
        int recolor = Integer.MAX_VALUE;

        for(int j=0; j<blocks.length(); j++){
            if(blocks.charAt(j) == 'W'){
                cw++;
            }

            if(j-i+1==k){
                recolor = Math.min(recolor, cw);
                if(blocks.charAt(i)=='W') cw--;
                i++;
            }
        }

        return recolor;
    }
}