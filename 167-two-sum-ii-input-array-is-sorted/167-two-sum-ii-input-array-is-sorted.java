class Solution {
    public int[] twoSum(int[] numbers, int target) {
        
        for(int i = 0 ; i < numbers.length-1 ; i++){
            int start = i+1;
            int end = numbers.length - 1;
            
            while(start <= end){
                int mid = start + (end-start)/2;
                if(mid != i && target - numbers[i] == numbers[mid]) {
                    return new int[]{i+1,mid+1};    
                }
                else if (target - numbers[i] > numbers[mid]) start = mid + 1;
                else end = mid - 1;
            }
            
            
        }
        
        return new int[2];
            
        
    }
}