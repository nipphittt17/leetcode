class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i,num in enumerate(nums):
            numbers[num] = i
        
        for i,num in enumerate(nums):
            num2 = target - num
            if num2 in numbers:
                if num2 != num:
                    return [i,numbers[num2]]
                elif numbers[num2] != i:
                    return [i,numbers[num2]]
                

                
                
        
            
        
        