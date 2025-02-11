class Solution {
    public boolean isPart(Stack s, String part, int n){
        Stack<Character> temp = new Stack<>();
        temp.addAll(s);

        for(int i=n-1; i>=0; i--){
            if(temp.pop()!=part.charAt(i)){
                return false;
            }
        }

        return true;
    }

    public String removeOccurrences(String s, String part) {
        Stack<Character> stack = new Stack<>();
        int p = part.length();

        for(int i=0; i<s.length(); i++){
            stack.add(s.charAt(i));

            if(stack.size()>=part.length() && isPart(stack, part, p)){
                for(int j=0; j<p; j++){
                    stack.pop();
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        while(!stack.isEmpty()){
            sb.append(stack.pop());
        }
        sb.reverse();

        return sb.toString();
    }
}