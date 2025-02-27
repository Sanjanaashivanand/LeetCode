class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        int totalGas = 0;
        int totalCost = 0;
        int[] diff = new int[n];

        for(int i=0; i<n; i++){
            totalGas += gas[i];
            totalCost += cost[i];
            diff[i] = gas[i] - cost[i];
        }

        if(totalCost>totalGas) return -1;

        int sum = 0;
        int idx = 0;
        for(int i=0; i<n; i++){
            sum += diff[i];
            if(sum<0){
                sum = 0;
                idx = i+1;
            }
            if(i==n-1){
                break;
            }
        }

        return idx;
    }
}