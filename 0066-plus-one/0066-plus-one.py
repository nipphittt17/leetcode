class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if(digits[len(digits)-1] < 9):
            digits[len(digits)-1] = digits[len(digits)-1]+1
            
        elif len(digits) == 1: #in case len == 1
            digits.append(0)
            digits[len(digits)-2] = 1
            
        else:  
            digits[len(digits)-1] = 0
            digits[len(digits)-2] = digits[len(digits)-2]+1
            for i in range(len(digits)-2,0,-1):
                #in case len > 1
                if digits[i] > 9: 
                    digits[i] = 0
                    digits[i-1] = digits[i-1] + 1
            if(digits[0] > 9): 
                digits[0] = 0
                digits.insert(0,1)

        return digits
        