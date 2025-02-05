class Solution {
    public void dfs(int[][] image, int i, int j, int sc, int color){
        if(i<0 || i>=image.length || j<0 || j>=image[0].length || image[i][j]!=sc){
            return;
        }

        image[i][j] = color;
        dfs(image, i+1, j, sc, color);
        dfs(image, i-1, j, sc, color);
        dfs(image, i, j+1, sc, color);
        dfs(image, i, j-1, sc, color);
    }

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if(image[sr][sc] == color) return image;
        dfs(image, sr, sc, image[sr][sc], color);
        return image;
    }
}