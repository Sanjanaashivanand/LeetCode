class Solution {
    public String removeOccurrences(String s, String part) {
        while(s.contains(part)){
            int startIdx = s.indexOf(part);

            s = s.substring(0,startIdx) + s.substring(startIdx + part.length());
        }

        return s;
    }
}