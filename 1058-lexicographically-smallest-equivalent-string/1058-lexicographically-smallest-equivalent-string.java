class Solution {
    int parent[] = new int[26];

    private void union(int x, int y){
        x = find(x);
        y = find(y);

        if(x == y) return;

        if(x<y){
            parent[y] = x;
        }
        else{
            parent[x] = y;
        }
    }
    
    private int find(int x){
        if(parent[x] == x){
            return x;
        }
        return parent[x] = find(parent[x]);
    }

    public String smallestEquivalentString(String s1, String s2, String baseStr) {
        for(int i=0; i<26; i++){
            parent[i] = i;
        }

        for(int i=0; i<s1.length(); i++){
            union(s1.charAt(i)-'a', s2.charAt(i)-'a');
        }

        StringBuilder res = new StringBuilder();
        for(char c : baseStr.toCharArray()){
            res.append((char)(find(c-'a')+'a'));
        }

        return res.toString();
    }
}