class Solution {
    public String reverseVowels(String s) {
        StringBuilder sb = new StringBuilder(s);

        HashSet<Character> set = new HashSet<>();
        set.add('a');
        set.add('e');
        set.add('i');
        set.add('o');
        set.add('u');
        set.add('A');
        set.add('E');
        set.add('I');
        set.add('O');
        set.add('U');

        List<Integer> loc = new ArrayList<>();

        for(int i=0; i<s.length(); i++){
            if(set.contains(s.charAt(i))){
                loc.add(i);
            }
        }


        int n = loc.size();
        for(int i=0; i<n/2; i++){
            int left = loc.get(i);
            int right = loc.get(n-i-1);
            char temp = s.charAt(left);

            sb.setCharAt(left, s.charAt(right));
            sb.setCharAt(right, temp);
        }

        return sb.toString();
    }
}