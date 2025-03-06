class Solution {
    public String simplifyPath(String path) {
        String[] path_arr = path.split("/");
        Stack<String> stack = new Stack<>();

        for(String s: path_arr){
            if (s.equals("") || s.equals(".")) {
                continue;
            }

            if (s.equals("..")) {
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            } else {
                stack.push(s);
            }
        }

        StringBuilder sb = new StringBuilder();

        while(!stack.isEmpty()){
            sb.insert(0, "/" + stack.pop());
        }

        if(sb.length() == 0) return "/";
        return sb.toString();
    }
}