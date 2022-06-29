class Solution {
    public int[] twoSum(int[] numbers, int target) {
        
        int[] out = new int[2];
        
        for(int i = 0 ; i < numbers.length ; i++){
            
            int start = i+1;
            int end = numbers.length - 1;
            
            while(start <= end){
                int mid = start + (end-start)/2;
                if(mid != i && target - numbers[i] == numbers[mid]) {
                    out[0] = i+1;
                    out[1] = mid+1;
                    return out;    
                }
                else if (target - numbers[i] > numbers[mid]) start = mid + 1;
                else end = mid - 1;
            }
            
            
        }
        
        return out;
            
        
    }
}