class Solution {
    public int minimumLength(String s) {
        int[] map = new int[26];

        for(char c: s.toCharArray()){
            map[c-'a']++;
        }

        int count = 0;

        for(int i:map){
            if(i==0) continue;
            if(i%2==0){
                count+=i-2;
            }
            else{
                count+=i-1;
            }
        }

        return s.length()-count;
    }

    //3,4,5,6,7,8,9
    //1,2,2,2,
}