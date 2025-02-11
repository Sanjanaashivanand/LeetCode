class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }

        long rev = 0;
        long num = x;

        while(x!=0){
            rev = rev * 10 + x % 10;
            x = x/10;
        }

        while(num!=0 || rev!=0){
            if(num%10 != rev%10){
                return false;
            }
            num = num/10;
            rev = rev/10;
        }

        return true;

    }
}