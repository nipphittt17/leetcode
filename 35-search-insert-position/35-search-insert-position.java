class Solution {
    public int searchInsert(int[] nums, int target) {
        int first = 0;
        int last = nums.length - 1;
        int mid = 0; 
        
        while(first <= last){
            mid = first + (last-first)/2;
            
            if(nums[mid] == target) return mid;
            
            else if(nums[mid] > target) {
                if(mid == 0 || nums[mid-1] < target) return mid;
                last = mid - 1;
            }
            
            else if(nums[mid] < target) {
                if(mid == nums.length-1 || nums[mid+1] > target) return mid+1;
                first = mid + 1;
            }
            
        }
        
        
        return mid;
    }
}