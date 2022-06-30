class Solution {
    public int minimumCost(int[] cost) {
        
        int out = 0;
        
        Arrays.sort(cost);
        
        int j = 1;
        for(int i = cost.length-1; i >= 0 ; i--){
            if(j%3 != 0) out = out + cost[i];
            j++;
            
        }
        
        return out;
        
    }
}