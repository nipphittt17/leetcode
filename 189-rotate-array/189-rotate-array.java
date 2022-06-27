class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length; //in case that k > nums.size -> k will be the leftover
        
        reverse(0, nums.length-1, nums); //all
        reverse(0, k-1, nums); //left side
        reverse(k, nums.length-1, nums); //right side
    }
    
    public void reverse(int left, int right, int[] arr){
        while(left < right){
            swap(left,right,arr);
            left++;
            right--;
        }
    }
    
    public void swap(int a, int b, int[] arr){
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
    
}