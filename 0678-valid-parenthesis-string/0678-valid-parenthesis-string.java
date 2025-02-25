class Solution {
    public boolean checkValidString(String s) {
        Stack<Integer> open = new Stack<>();
        Stack<Integer> stars = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(') {
                open.push(i); 
            } else if (c == '*') {
                stars.push(i); 
            } else if (c == ')') {
                if (!open.isEmpty()) {
                    open.pop(); 
                } else if (!stars.isEmpty()) {
                    stars.pop(); 
                } else {
                    return false; // No match found
                }
            }
        }


        while (!open.isEmpty() && !stars.isEmpty()) {
            if (open.pop() > stars.pop()) {
                return false; 
            }
        }

        return open.isEmpty(); 
    }
}
