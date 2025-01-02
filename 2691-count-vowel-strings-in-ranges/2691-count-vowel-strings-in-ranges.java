class Solution {
    public int[] vowelStrings(String[] words, int[][] queries) {
        int[] isVol = new int[words.length];

        for(int i=0; i<words.length; i++){
            String s = words[i];
            char start = s.charAt(0);
            char end = s.charAt(s.length()-1);
            if((start=='a'||start=='e'||start=='i'||start=='o'||start=='u')&&
                (end=='a'||end=='e'||end=='i'||end=='o'||end=='u')){
                    if(i==0){
                        isVol[i] = 1;
                    }
                    else{
                        isVol[i] = isVol[i-1]+1;
                    }
                }
            else{
                if(i==0){
                        isVol[i] = 0;
                    }
                else{
                    isVol[i] = isVol[i-1];
                }
            }
        }

        int[] res = new int[queries.length];
        for(int i=0; i<queries.length; i++){
            if(queries[i][0]==0){
                res[i] = isVol[queries[i][1]];
            }
            else{
                res[i] = isVol[queries[i][1]] - isVol[queries[i][0]-1];
            }
        }

        return res;
        
    }
}