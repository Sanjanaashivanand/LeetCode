class Solution {
    public boolean checkInclusion(String s1, String s2) {
        HashMap<Character, Integer> map = new HashMap<>();

        for(char c:s1.toCharArray()){
            map.put(c, map.getOrDefault(c, 0)+1);
        }

        int i=0;
        int j = s1.length()-1;

        while(i <= j && j < s2.length()){
            if(map.containsKey(s2.charAt(i))){
                HashMap<Character, Integer> window = new HashMap<>();
                for(int k=i; k<=j; k++){
                    window.put(s2.charAt(k), window.getOrDefault(s2.charAt(k),0)+1);
                }
                if(window.equals(map)) return true;
            }
            i++;
            j++;
        }
        return false;
    }
}