class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        String[] str = s.split("\\s+");

        Stack<String> stack = new Stack<>();

        for(String st : str){
            stack.push(st);
        }

        StringBuilder sb = new StringBuilder();

        while(!stack.isEmpty()){
            String curr = stack.pop();
            if(curr == " ") continue;
            sb.append(curr);
            sb.append(" ");
        }

        sb.setLength(sb.length() - 1);
        return sb.toString();
    }
}