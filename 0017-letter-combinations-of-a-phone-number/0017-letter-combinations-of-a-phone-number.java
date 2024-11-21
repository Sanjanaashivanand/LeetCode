class Solution {
    List<String> res = new ArrayList<>();

    private void backtrack(HashMap<Integer, String> map, String s, int i, StringBuilder sb){
        if(i==s.length()){
            res.add(sb.toString());
            return;
        }

        int digit = (int)s.charAt(i) - '0';

        for(char c: map.get(digit).toCharArray()){
            sb.append(c);
            backtrack(map, s, i+1, sb);
            sb.deleteCharAt(sb.length()-1);
        }
    }

    public List<String> letterCombinations(String digits) {
        if(digits.length()==0) return res;
        
        HashMap<Integer,String> map=new HashMap<>();
        map.put(2,"abc");
        map.put(3,"def");
        map.put(4,"ghi");
        map.put(5,"jkl");
        map.put(6,"mno");
        map.put(7,"pqrs");
        map.put(8,"tuv");
        map.put(9,"wxyz");

        backtrack(map, digits, 0, new StringBuilder()); 

        return res;
    }
}