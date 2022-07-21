class Solution:


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1,-1]        
        if target not in nums:
            return output

        output[0] = nums.index(target)
        i = output[0]
        count = 0        
        while(nums[i] == target):
            count+=1
            i+=1
            if i>=len(nums):
                break
        if count == 1:
            output[1] = output[0]
            return output
        output[1] = output[0]+count-1
        return output

                
        
        