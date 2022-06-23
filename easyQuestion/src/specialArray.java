// package easyQuestion.src;

//1608. Special Array With X Elements Greater Than or Equal X
public class specialArray {

    public static int specialArray(int[] nums) {
        
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

    // public static int findSpecial_loop(int[] nums) {
        
    //     Arrays.sort(nums);   
    //     //loop through nums
    //     for(int i = 1 ; i <= nums.length ; i++){
            
    //         //find num that >= i 
    //         int count = 0;
    //         for(int j = 0  ; j < nums.length ; j++){
    //             if(nums[j] >= i) count++;
    //         }
    //         //if count = i -> return i
    //         if(count == i) return i;
    //     }    
    //     return -1;   
    // }

    public static void main(String[] args) {
            // int[] test1 = {3,5};
            // int out1 = specialArray(test1);
            // System.out.println(out1);

            int[] test2 = {0,4,3,0,4};
            int out2 = specialArray(test2);
            System.out.println(out2);

            // int[] test3 = {0,0};
            // int out3 = specialArray(test3);
            // System.out.println(out3);

    }
}


