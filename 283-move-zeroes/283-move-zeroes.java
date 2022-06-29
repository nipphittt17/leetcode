class Solution {
    public void moveZeroes(int[] nums) {
        
        int left = 0;
        int right = 0;
        for(int i = 0 ; i < nums.length ; i++){
            if(nums[i] != 0) {
                nums[left] = nums[i];
                left++;
            }
            else right++;
            if(left+right == nums.length) break;
        }
        for(int i = left ; i < nums.length ; i++){
            nums[i] = 0;
        }
        
    }
}