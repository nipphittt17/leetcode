class Solution {
    public boolean divideArray(int[] nums) {

        // Arrays.sort(nums);
        // for(int i = 0 ; i < nums.length ; i = i + 2){
        //     if(nums[i] != nums[i+1]) return false;
        // }
        // return true;
        
        HashSet<Integer> set = new HashSet<>();
        
        for (int i : nums) {
            if (set.contains(i)) {
                set.remove(i);
            } else {
                set.add(i);
            }
        }
        return set.isEmpty();
    

    }
    
    
}