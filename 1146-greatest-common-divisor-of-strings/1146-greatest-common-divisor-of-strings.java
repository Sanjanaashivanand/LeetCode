class Solution {
    public String gcdOfStrings(String str1, String str2) {
        int n = str1.length();
        int m = str2.length();

        if(m > n) return gcdOfStrings(str2, str1);

        int i = 0;
        int j = str2.length()-1;

        for(j=m; j>=0; j--){
            if(n % (j - i + 1) == 0 && m % (j - i + 1) == 0){
                String substring = str2.substring(i, j-i+1);

                int s1_chunks = n / (j-i+1);
                int s2_chunks = m / (j-i+1);

                StringBuilder sb1 = new StringBuilder();
                for(int k=0; k<s1_chunks; k++){
                    sb1.append(substring);
                }

                if(!sb1.toString().equals(str1)) break;

                StringBuilder sb2 = new StringBuilder();
                for(int k=0; k<s2_chunks; k++){
                    sb2.append(substring);
                }

                if(!sb2.toString().equals(str2)) break;

                return substring;
            }
        }

        return "";
    }
}