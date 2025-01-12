class Solution {
    public boolean canBeValid(String s, String locked) {
        int n = s.length();

        if(n%2!=0) return false;

        Stack<Integer> openBracket = new Stack<>();
        Stack<Integer> unlocked = new Stack<>();

        for(int i=0; i<n; i++){
            if(locked.charAt(i)=='0'){
                unlocked.push(i);
            }
            else if(s.charAt(i)=='('){
                openBracket.push(i);
            }
            else if(s.charAt(i)==')'){
                if(!openBracket.isEmpty()){
                    openBracket.pop();
                }
                else if(!unlocked.isEmpty()){
                    unlocked.pop();
                }
                else{
                    return false;
                }
            }
        }

        while(!openBracket.isEmpty() &&
            !unlocked.isEmpty() &&
            openBracket.peek()<unlocked.peek()){
                openBracket.pop();
                unlocked.pop();
            }

        return openBracket.isEmpty();
    }
}