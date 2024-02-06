class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<ArrayList<Integer>, ArrayList<String>> map = new HashMap<>();

        for(String s:strs){
            ArrayList<Integer> count = new ArrayList<Integer>(Collections.nCopies(26, 0));

            for(char c : s.toCharArray()){
                count.set((int)c - 'a',count.get((int)c - 'a')+1);
            }
            if(!map.containsKey(count)){
                ArrayList<String> val = new ArrayList<>();
                val.add(s);
                map.put(count, val);
            }
            else{
                ArrayList<String> val = map.get(count);
                val.add(s);
                map.put(count, val);
            }

        }

        List<List<String>> res = new ArrayList<>(map.values());
        return res;

    }
}