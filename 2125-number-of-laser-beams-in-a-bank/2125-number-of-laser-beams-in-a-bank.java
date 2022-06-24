class Solution {
    public int numberOfBeams(String[] bank) { 
        
        int[] count = new int[bank.length];
        
        for(int i = 0 ; i < bank.length ; i++){
            for(int j = 0 ; j < bank[i].length() ; j++){
                //count 1
                if(bank[i].charAt(j) == '1') count[i]++;
            }
        }
        
        //return 0 if only 1 row contain 1
        
        int ans = 0;
        int empty = 0;
        int mul = 0;
        
        for(int i = 0 ; i < count.length ; i++){
            if(count[i] == 0) empty++;
            else{
 
                if(mul != 0){
                    ans = ans + count[i] * mul; 
                }
                
                mul = count[i];
    
            }
            if(empty >= count.length-1) return 0;
        }
        
        return ans;
    }
}