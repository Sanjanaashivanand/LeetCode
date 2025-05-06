class Solution {
    public int minMutation(String startGene, String endGene, String[] bankArray) {
        Queue<String> q = new LinkedList<>();
        HashSet<String> vis = new HashSet<>();
        char[] chars = new char[]{'A', 'C', 'G', 'T'};
        HashSet<String> bank = new HashSet<>();

        q.offer(startGene);
        vis.add(startGene);

        for(String s: bankArray) bank.add(s);

        int count = 0;

        while(!q.isEmpty()){
            int len = q.size();
            System.out.println(q);

            for(int i=0; i<len; i++){
                String curr = q.poll();

                if(curr.equals(endGene)){
                    return count;
                }

                for(int j=0; j<curr.length(); j++){
                    for(char c : chars){
                        StringBuilder sb = new StringBuilder(curr);
                        sb.setCharAt(j, c);

                        if(bank.contains(sb.toString()) && 
                        !vis.contains(sb.toString())){
                            q.offer(sb.toString());
                            vis.add(sb.toString());
                        }
                    }
                }

            }

            count++;
        }

        return -1;
    }
}