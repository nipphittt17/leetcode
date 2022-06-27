class Solution {
    public static void swap(int a, int b){
        int temp = a;
        a = b;
        b = temp;
    }
    
    public int[] sortedSquares(int[] nums) {
        
        for(int i = 0 ; i < nums.length ; i++){
            nums[i] = (int)Math.pow(nums[i],2);
        }
        
        // Arrays.sort(nums);
        

        for(int i = 1 ; i < nums.length ; i++){
            int key = nums[i];
            int j = i-1;

            while(j >= 0 && nums[j] > key){
                nums[j+1] = nums[j];
                j--;
            }

            nums[j+1] = key;
        }
        
        
        return nums;
    }
}