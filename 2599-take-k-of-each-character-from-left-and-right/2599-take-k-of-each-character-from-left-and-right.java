class Solution {
    public int takeCharacters(String s, int k) {
        if (k == 0) return 0;

        int n = s.length();
        int[] total = new int[3];

        // Count the total occurrences of 'a', 'b', 'c'
        for (char c : s.toCharArray()) {
            total[c - 'a']++;
        }

        // Check if it is even possible to take k of each character
        for (int i = 0; i < 3; i++) {
            if (total[i] < k) return -1;
        }

        // Sliding window to find the longest valid substring we can leave behind
        int[] window = new int[3];
        int maxValidWindow = 0;
        int left = 0;

        for (int right = 0; right < n; right++) {
            // Add current character to the window
            window[s.charAt(right) - 'a']++;

            // Shrink the window from the left if it is invalid
            while (window[0] > total[0] - k || window[1] > total[1] - k || window[2] > total[2] - k) {
                window[s.charAt(left) - 'a']--;
                left++;
            }

            // Update the maximum valid window size
            maxValidWindow = Math.max(maxValidWindow, right - left + 1);
        }

        // The result is the length of the string minus the longest valid window
        return n - maxValidWindow;
    }
}
