class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> res = new ArrayList<>();
        
        if (s == null || words == null || words.length == 0 || s.length() < words.length * words[0].length()) {
            return res;
        }

        int wordLen = words[0].length();
        int totalLen = wordLen * words.length;
        
        // Step 1: Build frequency map for words
        Map<String, Integer> wordCount = new HashMap<>();
        for (String word : words) {
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }

        // Step 2: Sliding window over the string s
        for (int i = 0; i < wordLen; i++) {
            int left = i, right = i, count = 0;
            Map<String, Integer> windowCount = new HashMap<>();

            while (right + wordLen <= s.length()) {
                // Get the word from the substring
                String word = s.substring(right, right + wordLen);
                right += wordLen;
                
                // If the word is in the original list of words
                if (wordCount.containsKey(word)) {
                    windowCount.put(word, windowCount.getOrDefault(word, 0) + 1);
                    count++;

                    // If the frequency exceeds the target, move the left pointer
                    while (windowCount.get(word) > wordCount.get(word)) {
                        String leftWord = s.substring(left, left + wordLen);
                        windowCount.put(leftWord, windowCount.get(leftWord) - 1);
                        left += wordLen;
                        count--;
                    }

                    // If we have the correct number of words in the window, add the starting index
                    if (count == words.length) {
                        res.add(left);
                    }
                } else {
                    // If the word is not in the original words list, reset the window
                    windowCount.clear();
                    count = 0;
                    left = right;
                }
            }
        }

        return res;
    }
}
