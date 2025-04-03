class Solution {
    class Pair{
        int idx;
        int height;

        Pair(int idx, int height){
            this.idx = idx;
            this.height = height;
        }
    }

    public int largestRectangleArea(int[] heights) {
        Stack<Pair> stack = new Stack<>();
        int max = 0;

        for(int i=0; i<heights.length; i++){
            int startIdx = i;

            while(!stack.isEmpty() && stack.peek().height > heights[i]){
                Pair top = stack.pop();
                max = Math.max(max, top.height * (i - top.idx));
                startIdx = top.idx;
            }

            stack.push(new Pair(startIdx, heights[i]));
        }

        while(!stack.isEmpty()){
            Pair top = stack.pop();
            max = Math.max(max, top.height * (heights.length - top.idx));
        }

        return max;
    }
}