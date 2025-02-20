class Solution {
    private String backtrack(int idx, StringBuilder sb, HashSet<String> set, int n) {
        if (idx == n) {
            String candidate = sb.toString();
            return set.contains(candidate) ? "" : candidate;
        }

        // Try '0' first
        sb.setCharAt(idx, '0');
        String res = backtrack(idx + 1, sb, set, n);
        if (!res.isEmpty()) return res;

        // Try '1' if '0' doesn't work
        sb.setCharAt(idx, '1');
        res = backtrack(idx + 1, sb, set, n);
        if (!res.isEmpty()) return res;

        return "";
    }

    public String findDifferentBinaryString(String[] nums) {
        if(nums.length==0){
            return "";
        }

        HashSet<String> set = new HashSet<>();
        for(String s:nums){
            set.add(s);
        }

        StringBuilder sb = new StringBuilder();

        for(int i=0; i<nums[0].length(); i++){
            sb.append('0');
        }

        return backtrack(0, sb, set, nums[0].length());
    }
}