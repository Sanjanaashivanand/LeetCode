class WordDictionary {
    class Node{
        Node[] links;
        boolean flag;

        public Node(){
            links = new Node[26];
            flag = false;
        }
    }

    private Node root;

    public WordDictionary() {
        root = new Node();
    }
    
    public void addWord(String word) {
        Node curr = root;
        for(char c:word.toCharArray()){
            int idx = c - 'a';
            if(curr.links[idx]==null){
                curr.links[idx] = new Node();
            }
            curr = curr.links[idx];
        }
        curr.flag = true;
    }
    
    public boolean search(String word) {
        return find(0, word.toCharArray(), root);
    }

    private boolean find(int idx, char[] charArray, Node curr){
        if(idx==charArray.length) return curr.flag;
        char c = charArray[idx];

        if(c=='.'){
            for(Node child: curr.links){
                if(child!=null && 
                    find(idx+1, charArray, child)){
                        return true;
                }
            }
            return false;
        }
        else{
            int i = c - 'a';
            if(curr.links[i]==null) return false;
            return find(idx+1, charArray, curr.links[i]);
        }
    }
}


/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */