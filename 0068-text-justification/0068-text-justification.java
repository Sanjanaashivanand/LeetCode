class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        int n = words.length;
        List<String> res = new ArrayList<>();
        int i = 0;

        while (i < n) {
            int currLen = 0;
            int count = 0;

            // Determine how many words can fit on the current line
            int j = i;
            while (j < n && currLen + words[j].length() + count <= maxWidth) {
                currLen += words[j].length();
                count++;
                j++;
            }

            // Handle the case for a single word in a line or the last line
            StringBuilder sb = new StringBuilder();
            int spaces = maxWidth - currLen;
            if (count == 1 || j == n) { // Single word or last line
                for (int k = i; k < j; k++) {
                    sb.append(words[k]);
                    if (k < j - 1) {
                        sb.append(" ");
                    }
                }
                while (sb.length() < maxWidth) {
                    sb.append(" ");
                }
            } else {
                // Regular line with multiple words
                int between = spaces / (count - 1);
                int extra = spaces % (count - 1);
                for (int k = i; k < j; k++) {
                    sb.append(words[k]);
                    if (k < j - 1) {
                        int spacesToAdd = between + (k - i < extra ? 1 : 0);
                        for (int x = 0; x < spacesToAdd; x++) {
                            sb.append(" ");
                        }
                    }
                }
            }

            res.add(sb.toString());
            i = j;
        }

        return res;
    }
}
