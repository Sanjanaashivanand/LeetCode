class Solution {
    public int reverse(int x) {
        long res = 0;

        while(x!=0){
            int digit = x%10;
            res = (res * 10) + digit;
            x = x/10;
        }

        if(res<Integer.MIN_VALUE|| res>Integer.MAX_VALUE) return 0;

        return (int)res;
    }
}