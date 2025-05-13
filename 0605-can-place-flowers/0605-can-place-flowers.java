class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0) return true;

        if(flowerbed.length==1){
            if(n==1 && flowerbed[0]==0){
                return true;
            }
            return false;
        }
        
        for(int i=0; i<flowerbed.length; i++){
            if(flowerbed[i] == 1) continue;

            if(i==0){
                if(flowerbed[1]==0){
                    flowerbed[0] = 1;
                    n--; 
                }
            }
            else if(i==flowerbed.length-1){
                if(flowerbed[flowerbed.length-2]==0){
                    flowerbed[flowerbed.length-1] = 1;
                    n--; 
                }
            }
            else{
                if(flowerbed[i-1] == 0 && flowerbed[i+1] == 0){
                    flowerbed[i] = 1;
                    n--;
                }
            }
        }

        return n<=0;
    }
}