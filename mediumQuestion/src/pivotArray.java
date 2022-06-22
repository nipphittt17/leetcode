public class pivotArray {

    //2161. Partition Array According to Given Pivot

    public int[] pivotArray(int[] nums, int pivot) {

        int[] out = new int[nums.length];
        int left = 0;
        // int right = nums.length - 1;

        for(int i = 0 ; i < nums.length ; i++){
            if(nums[i] < pivot){
                out[left] = nums[i];
                left++;
            }
        }
        
        for(int i = 0 ; i < nums.length ; i++){
            if(nums[i] == pivot){
                out[left] = nums[i];
                left++;
            }
        }
        
        for(int i = 0 ; i < nums.length ; i++){
            if(nums[i] > pivot){
                out[left] = nums[i];
                left++;
            }
        }


        return out;
        
    }
}
