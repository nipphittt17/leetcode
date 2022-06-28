class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        
        int time = 0;
        
        for(int i = 0 ; i < points.length-1 ; i++){
         
            int[] cur = points[i];
            int[] prev = points[i+1];
            int curVal = Math.max(Math.abs(cur[0] - prev[0]), Math.abs(cur[1] - prev[1]));
            time += curVal;
        }
        
        return time;
        
    }
}