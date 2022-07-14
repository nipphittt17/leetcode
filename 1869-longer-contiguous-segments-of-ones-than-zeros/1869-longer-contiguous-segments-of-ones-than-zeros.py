class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        one = 0
        zero = 0
        
        now = ' '
        
        longOne = 0
        longZero = 0
        
        for char in s:
            
            if now == '1':
                if char == '1':
                    now = '1'       
                else:
                    if one > longOne:
                        longOne = one
                    one = 0
                    now = '0'
                                       
            elif now == '0':
                if char == '1':
                    if zero > longZero:
                        longZero = zero
                    zero = 0
                    now = '1'
                else:
                    now = '0'            
            
            if char == '1':
                one+=1
                now = '1'
                
            else:
                zero+=1
                now = '0' 
                
        if zero > longZero:
            longZero = zero
        if one > longOne:
            longOne = one          

        if longOne > longZero:
            return True
        else:
            return False

        return 0
                
         
        