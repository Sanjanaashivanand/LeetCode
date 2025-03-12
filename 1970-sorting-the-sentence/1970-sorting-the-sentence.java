class Solution {
    public String sortSentence(String string) {
        Map<Integer, String> map = new TreeMap<>();
        String[] strs = string.split(" ");

        for(String s:strs){
            int idx = s.charAt(s.length() - 1) - '0';
            map.put(idx, s.substring(0, s.length()-1));
        }

        StringBuilder sb = new StringBuilder();
        for(int i : map.keySet()){
            sb.append(map.get(i));
            sb.append(" ");
        }

        sb.setLength(sb.length() - 1);
        return sb.toString();
    }
}