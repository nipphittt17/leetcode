class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length; //
        
        reverse(0, nums.length-1, nums); //all
        reverse(0, k-1, nums); //left side
        reverse(k, nums.length-1, nums); //right side
    }
    
    public void reverse(int left, int right, int[] arr){
        while(left < right){
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            
            left++;
            right--;
        }
    }
    
}