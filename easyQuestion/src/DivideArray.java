package easyQuestion.src;

import java.util.HashSet;

//2206. Divide Array Into Equal Pairs

public class DivideArray {
    public static boolean divideArray(int[] nums) {

        //using sorted array
        // Arrays.sort(nums);
        // for(int i = 0 ; i < nums.length ; i = i + 2){
        //     if(nums[i] != nums[i+1]) return false;
        // }
        // return true;
        
        //using hashset: add and remove (it's even element)
        HashSet<Integer> set = new HashSet<>();
        
        for (int i : nums) {
            if (set.contains(i)) {
                set.remove(i);
            } else {
                set.add(i);
            }
        }
        //if the num is 2 -> set will be empty
        return set.isEmpty();
    }

    public static void main(String[] args) {
        int[] test1 = {3,2,3,2,2,2};
        boolean ans1 = divideArray(test1);
        System.out.println(ans1);
    }
    
}
