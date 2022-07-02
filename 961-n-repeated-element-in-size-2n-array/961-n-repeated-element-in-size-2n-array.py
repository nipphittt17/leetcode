class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        digits = {
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
            6 : 0,
            7 : 0,
            8 : 0,
            9 : 0,
            0 : 0,
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
            
            
        