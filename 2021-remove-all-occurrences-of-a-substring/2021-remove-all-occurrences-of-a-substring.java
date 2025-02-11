class Solution {
    public boolean isPart(Stack s, String part){
        Stack<Character> temp = new Stack<>();
        temp.addAll(s);

        for(int i=part.length()-1; i>=0; i--){
            if(temp.pop()!=part.charAt(i)){
                return false;
            }
        }

        return true;
    }

    public String removeOccurrences(String s, String part) {
        Stack<Character> stack = new Stack<>();

        for(int i=0; i<s.length(); i++){
            stack.add(s.charAt(i));

            if(stack.size()>=part.length() && isPart(stack, part)){
                for(int j=0; j<part.length(); j++){
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