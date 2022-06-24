class Solution {
        public int climbStairs(int n) {
            
            if(n == 1 || n == 2) return n;
            int first = 1, second = 2, step = 0;
            
            for(int i = 2 ; i < n ; i++){
                step = first+second;
                first = second;
                second = step;
                
            }
            
            return step;
        }
}