class Solution {

     public int specialArray(int[] nums) {
        int begin = 0;
        int last = nums.length;
        int ans = -1;
        
        while(begin <= last) {
            int mid = begin + (last-begin)/2;
            
            int count = 0;
            for (int i = 0; i < nums.length ; i++) {
                if (nums[i] >= mid) {
                    count++;
                }
            }
            if (mid == count) {
                ans = mid;
                begin = mid + 1;
            } else if (mid > count) {
                last = mid - 1;
            } else {
                begin = mid + 1;
            }
        }
        
        return ans;
    }
}