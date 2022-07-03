class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        out = 0
        digits = {}
        
        for i,x in enumerate(nums):
            if x in digits:     
                for index in digits[x]:
                    if (index*i)%k == 0:
                        out += 1    
                digits[x].append(i)
            else:
                digits[x] = [i]
                
        return out    
            
        