class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        Arrays.sort(citations);

        int i = 0;
        while (i < n && citations[n - 1 - i] > i) {
            i++;
        }
        return i; 
    }
}