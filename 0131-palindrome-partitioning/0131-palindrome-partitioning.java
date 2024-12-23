class Solution {
    private List<List<String>> res = new ArrayList<>();

    private boolean isPali(String s, int l, int r){
        while(l<r){
            if(s.charAt(l)!=s.charAt(r)){
                return false;
            }
            l++;
            r--;
        }

        return true;
    }

    private void backtrack(String s, int start, List<String> path) {
        if(start == s.length()){
            res.add(new ArrayList<>(path));
            return;
        }

        for(int end=start+1; end<=s.length(); end++){
            if(isPali(s, start, end-1)){
                path.add(s.substring(start,end));
                backtrack(s, end, path);
                path.remove(path.size()-1);
            }
        }
    }

    public List<List<String>> partition(String s) {
        backtrack(s, 0, new ArrayList<>());
        return res;
    }
}