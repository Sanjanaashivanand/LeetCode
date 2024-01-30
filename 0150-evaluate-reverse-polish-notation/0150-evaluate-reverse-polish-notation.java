class Solution {
    public int evalRPN(String[] tokens) {
        if(tokens.length == 1) return Integer.parseInt(tokens[0]);
        Stack<Integer> digits = new Stack<Integer>();
        
        for(int i=0; i<tokens.length;i++){
            if(tokens[i].equals("*")){
                int a = digits.pop();
                int b = digits.pop();
                digits.push(a*b);
            }
            else if(tokens[i].equals("/")){
                int a = digits.pop();
                int b = digits.pop();
                digits.push(b/a);
            }
            else if(tokens[i].equals("+")){
                int a = digits.pop();
                int b = digits.pop();
                digits.push(a+b);
            }
            else if(tokens[i].equals("-")){
                int a = digits.pop();
                int b = digits.pop();
                digits.push(b-a);
            }
            else{
                digits.push(Integer.parseInt(tokens[i]));
            }
        }

        return digits.pop();
    }
}