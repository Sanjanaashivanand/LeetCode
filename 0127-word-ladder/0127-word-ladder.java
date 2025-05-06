class Solution {
    private class Pair{
        String word;
        int dis;

        Pair(String word, int dis){
            this.word = word;
            this.dis = dis;
        }
    }

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        HashSet<String> wordSet= new HashSet<>(wordList);

        Queue<Pair> q = new LinkedList<>();
        q.offer(new Pair(beginWord, 1));
        wordSet.remove(beginWord);

        while(!q.isEmpty()){
            Pair curr = q.poll();

            if(curr.word.equals(endWord)){
                return curr.dis;
            }
            
            for(int i=0; i<curr.word.length(); i++){
                StringBuilder sb = new StringBuilder(curr.word);    
                for(char c='a'; c<='z'; c++){
                    sb.setCharAt(i, c);
                    String check = sb.toString();
                    if(wordSet.contains(check)){
                        q.offer(new Pair(check, curr.dis+1));
                        wordSet.remove(check);
                    }
                }
            }

            
        }

        return 0;
    }
}