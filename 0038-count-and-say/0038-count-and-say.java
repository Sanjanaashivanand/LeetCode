class Solution {
    public String countAndSay(int n) {
        if(n == 1){
            return "1";
        }

        StringBuilder sb = new StringBuilder();
        String prev = countAndSay(n-1);

        int count = 1;
        for(int i=0; i<prev.length()-1; i++){
            if(prev.charAt(i) == prev.charAt(i+1)){
                count++;
            }
            else{
                sb.append(count);
                sb.append(prev.charAt(i));
                count = 1;
            }
        }

        sb.append(count);
        sb.append(prev.charAt(prev.length()-1));
        

        return sb.toString();
    }
}