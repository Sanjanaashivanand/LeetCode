class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        // Initialize maps for frequency of each character in words1 and words2
        HashMap<String, ArrayList<Integer>> map1 = new HashMap<>();
        
        // Frequency map for words2 - track the max frequency of characters across all words in words2
        ArrayList<Integer> maxFreq2 = new ArrayList<>(Collections.nCopies(26, 0));

        // Calculate the frequency map for each word in words1
        for(String word : words1) {
            if (!map1.containsKey(word)) {
                map1.put(word, new ArrayList<Integer>(Collections.nCopies(26, 0)));
            }

            ArrayList<Integer> arr = map1.get(word);
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                arr.set(c - 'a', arr.get(c - 'a') + 1);
            }
        }

        // Calculate the max frequency of characters across all words in words2
        for(String word : words2) {
            ArrayList<Integer> arr2 = new ArrayList<>(Collections.nCopies(26, 0));
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                arr2.set(c - 'a', arr2.get(c - 'a') + 1);
            }
            // Update the max frequency array for each character
            for (int i = 0; i < 26; i++) {
                maxFreq2.set(i, Math.max(maxFreq2.get(i), arr2.get(i)));
            }
        }

        // List to store the result
        ArrayList<String> res = new ArrayList<>();

        // Check each word in words1
        for(String s1: map1.keySet()){
            ArrayList<Integer> word1Array = map1.get(s1);
            boolean isValid = true;
            
            // Compare word1Array (for s1) with the maxFreq2 array (from words2)
            for(int i = 0; i < 26; i++) {
                if (word1Array.get(i) < maxFreq2.get(i)) {
                    isValid = false;
                    break;
                }
            }

            // If the word is valid, add it to the result list
            if (isValid) {
                res.add(s1);
            }
        }

        return res;
    }
}
