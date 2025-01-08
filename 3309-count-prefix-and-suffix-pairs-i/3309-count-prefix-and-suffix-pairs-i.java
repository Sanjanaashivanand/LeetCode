class Solution {
    public int countPrefixSuffixPairs(String[] words) {
        int res = 0;

        for(int i=0; i<words.length; i++){
            for(int j=i+1; j<words.length; j++){
                int prefix = words[j].indexOf(words[i]);
                int sufix = words[j].lastIndexOf(words[i]);
                if(prefix==0 && sufix==words[j].length()-words[i].length()){
                    res++;
                }
            }
        }

        return res;
        
    }
}