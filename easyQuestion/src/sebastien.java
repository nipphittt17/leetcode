public class sebastien{
    // public boolean checkPossibility(int[] nums) {
  
    //     if(check(nums) == false) {
    //         for(int i  = 0 ; i < nums.length-1 ; i++){
    //             int temp = nums[i];
    //             nums[i] = nums[i+1];
                
    //             if(check(nums) == true) return true;
    //             else nums[i] = temp;
    //         } 
            
    //         if(nums[nums.length - 1] < nums[nums.length - 2]){
    //             nums[nums.length - 1] = nums[nums.length - 2];
    //             if(check(nums) == true) return true;
    //         }
    //         return false;
    //     }
    //     return true;  
    // }

    


    // public boolean check(int[] nums){

    //     int status = 0;

    //     for(int i = 0 ; i < nums.length-1 ; i++){
    //         if(nums[i] > nums[i+1]) status = 1;
    //     }

    //     if(status == 0) return true;
    //     return false;
    // }
    
    public boolean checkPossibility(int[] nums) {
    
        for (int i = 1, modified = 0; i < nums.length ; i++) {
            if (nums[i-1] > nums[i]) {
                if (modified++ == 1) return false;
                
                if (i < 2 || nums[i-2] <= nums[i]) nums[i-1] = nums[i];
                
                else nums[i] = nums[i-1];
            }
        }
        return true;
    }

}   