import java.util.*;

class Solution {
    public int maximumSum(int[] nums) {
        Map<Integer, Integer> sumToMaxNum = new HashMap<>();
        int res = -1;

        for (int num : nums) {
            int digitSum = getDigitSum(num);
            if (sumToMaxNum.containsKey(digitSum)) {
                res = Math.max(res, sumToMaxNum.get(digitSum) + num);
            }
            sumToMaxNum.put(digitSum, Math.max(sumToMaxNum.getOrDefault(digitSum, 0),num));
        }
        return res;
    }

    
    private int getDigitSum(int num) {
        int sum = 0;
        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
