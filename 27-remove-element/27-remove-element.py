class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0
        for num in nums:
            if num == val:
                count+=1
    
        for i in range(count):
            nums.remove(val)
        # i = 0
        # while val in nums:
        #     if nums[i] == val:
        #         nums.pop(i)
        #     else:
        #         i+=1
                
        return len(nums)
        