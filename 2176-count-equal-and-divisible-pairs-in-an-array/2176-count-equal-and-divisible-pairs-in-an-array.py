class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        out = 0
        
        for i in range(len(nums)):
            if(nums.count(nums[i]) > 1):
                for j in range(i+1,len(nums)):
                    if(nums[i] == nums[j] and (i*j)%k == 0):
                        out += 1
                
        return out    
            
        