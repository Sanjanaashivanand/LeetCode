class Solution {
    public int minSteps(String s, String t) {
        HashMap<Character, Integer> s_map = new HashMap<Character, Integer>();
        for(int i=0; i<s.length(); i++){
            s_map.put(s.charAt(i), s_map.getOrDefault(s.charAt(i),0)+1);
        }

        int count = 0;
        for(char t_char : t.toCharArray()){
            if(s_map.containsKey(t_char)){
                if(s_map.get(t_char)==1){
                    s_map.remove(t_char);
                }
                else{
                    s_map.put(t_char,s_map.get(t_char)-1);
                }
            }
            else{
                count++;
            }
        }

        return count;
    }
}