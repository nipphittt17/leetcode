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

//                 int h1 = points[i][0];
//                 int h2 = points[i+1][0];
//                 int v1 = points[i][1];
//                 int v2 = points[i+1][1];
                
//                 //horizon
//                 time = time + (int)Math.abs(h2 - h1);
                
                    
//                 //vertical
//                 if(Math.abs(v2-v1) > Math.abs(h2-h1)) {
//                     v1 = h2;     
//                     time = time + (v2-v1);
//                 }   

//         }