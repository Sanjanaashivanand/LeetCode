class Solution {
    public boolean isValid(String str) {
        Stack<Character> s = new Stack<>();

        for(char c : str.toCharArray()){
            if(c=='(' || c=='{' || c=='['){
                s.push(c);
            }
            else if(s.isEmpty() || s.peek() == '(' && c!=')' || s.peek()=='{' && c!='}' || s.peek()=='[' && c!=']'){
                return false;
            }
            else{
                s.pop();
            }
        }

        return s.isEmpty();
    }
}