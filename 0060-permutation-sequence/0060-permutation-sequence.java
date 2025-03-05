class Solution {
    public void generateNext(StringBuilder sb, int n) {
        int breakPoint = -1;

        // Find the first decreasing element from the right
        for (int i = n - 2; i >= 0; i--) {
            if (sb.charAt(i) < sb.charAt(i + 1)) {
                breakPoint = i;
                break;
            }
        }

        // If no such element is found, the current permutation is the last one, so we reverse the string
        if (breakPoint == -1) {
            sb.reverse();
            return;
        }

        // Find the smallest element that is larger than sb[breakPoint] from the right of breakPoint
        int next = -1;
        for (int i = n - 1; i > breakPoint; i--) {
            if (sb.charAt(i) > sb.charAt(breakPoint)) {
                next = i;
                break;
            }
        }

        // Swap the characters
        char temp = sb.charAt(breakPoint);
        sb.setCharAt(breakPoint, sb.charAt(next));
        sb.setCharAt(next, temp);

        // Reverse the part of the string after the breakPoint
        StringBuilder left = new StringBuilder(sb.substring(0, breakPoint + 1));
        StringBuilder right = new StringBuilder(sb.substring(breakPoint + 1));
        right.reverse();  // Reverse the right part
        sb.setLength(0);  // Clear the StringBuilder
        sb.append(left).append(right);  // Append both parts
    }

    public String getPermutation(int n, int k) {
        StringBuilder sb = new StringBuilder();
        
        // Initialize the string with numbers from 1 to n
        for (int i = 1; i <= n; i++) {
            sb.append(i);
        }

        // Generate the k-th permutation
        for (int i = 1; i < k; i++) {
            generateNext(sb, n);
        }

        return sb.toString();
    }
}
