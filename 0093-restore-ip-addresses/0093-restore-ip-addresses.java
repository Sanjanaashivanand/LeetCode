class Solution {
    List<String> res;
    
    private boolean valid(String s, int start, int length) {
        return (
            length == 1 ||
            (s.charAt(start) != '0' &&
                (length < 3 ||
                    s.substring(start, start + length).compareTo("255") <= 0))
        );
    }

    public void helper(String s, int curr, List<Integer> dots){
        int remainingLength = s.length() - curr;
        int remainingNumberOfIntegers = 4 - dots.size();

        if (remainingLength > remainingNumberOfIntegers * 3 ||
            remainingLength < remainingNumberOfIntegers) {
            return;
        }

        if(dots.size()==3){
            if(valid(s, curr, remainingLength)){
                StringBuilder sb = new StringBuilder();
                int last = 0;
                for (Integer dot : dots) {
                    sb.append(s.substring(last, last + dot));
                    last += dot;
                    sb.append('.');
                }
                sb.append(s.substring(curr));
                res.add(sb.toString());
            }
            return;
        }

        for(int i=1; i<=3; i++){
            if(i>remainingLength) break;

            dots.add(i);

            if(valid(s, curr, i)){
                helper(s, curr + i, dots);
            }

            dots.remove(dots.size() - 1);
        }
    }

    public List<String> restoreIpAddresses(String s) {
        res = new ArrayList<>();
        helper(s, 0, new ArrayList<>());
        return res;
    }
}