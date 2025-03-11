class Solution {
    public long atleast(String s, int k){
        long res = 0;
        int start = 0, end = 0;
        HashSet<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');

        HashMap<Character, Integer> vowelCount = new HashMap<>();
        int conso = 0;

        while(end < s.length()){
            char right = s.charAt(end);

            if(vowels.contains(right)){
                vowelCount.put(right, vowelCount.getOrDefault(right, 0) + 1);
            }
            else{
                conso++;
            }

            while(vowelCount.size() == 5 && conso >= k){
                res += s.length() - end;
                char left = s.charAt(start);

                if(vowels.contains(left)){
                    if(vowelCount.get(left) == 1){
                        vowelCount.remove(left);
                    }
                    else{
                        vowelCount.put(left, vowelCount.getOrDefault(left, 0) - 1);
                    }   
                }
                else{
                    conso--;
                }
                start++;
            }
            end++;
        }

        return res;
    }

    public long countOfSubstrings(String word, int k) {
        return atleast(word, k) - atleast(word, k+1);
    }
}
