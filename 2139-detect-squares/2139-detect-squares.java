import java.util.*;

class DetectSquares {
    private HashMap<String, Integer> points;

    public DetectSquares() {
        this.points = new HashMap<>();
    }
    
    
    public void add(int[] point) {
        String key = point[0] + "," + point[1];
        points.put(key, points.getOrDefault(key, 0) + 1);
    }
    
    
    public int count(int[] point) {
        int count = 0;
        int px = point[0];
        int py = point[1];

        
        for (String key : points.keySet()) {
            String[] coords = key.split(",");
            int x = Integer.parseInt(coords[0]);
            int y = Integer.parseInt(coords[1]);

            
            if (Math.abs(px - x) != Math.abs(py - y) || x == px || y == py) {
                continue;  
            }

            count += points.getOrDefault(x + "," + py, 0) * points.getOrDefault(px + "," + y, 0)
                    * points.get(key);
        }

        return count;
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares obj = new DetectSquares();
 * obj.add(point);
 * int param_2 = obj.count(point);
 */
