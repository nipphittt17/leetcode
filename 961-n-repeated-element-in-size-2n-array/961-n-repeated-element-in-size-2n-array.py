class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        digits = {

        }
        
        n = len(nums)/2
        
        for num in nums:    
            if num in digits:
                digits[num] = digits.get(num) + 1
            else:
                digits[num] = 1
         
        for digit in digits:
            if digits.get(digit) == n:
                return digit
            
            
        