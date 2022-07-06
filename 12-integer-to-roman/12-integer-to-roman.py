class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        
        out = ""
     
        for roman in romans:
            if num == roman:
                return romans[roman]
            
            
        num_str = str(num)   
        length = len(num_str)
        
        for i in range(length-1,-1,-1):
            r = 10**(length-i-1)
            
            if num_str[i] == '4' or num_str[i] == '9':
                out = romans[r] + romans[(int(num_str[i])+1)*r] + out
                
            elif num_str[i] < '4':
                temp = int(num_str[i])
                while(temp>0):
                    out = romans[r] + out
                    temp-=1
                    
            elif num_str[i] >= '5':
                temp = int(num_str[i])-5
                while(temp>0):
                    out = romans[r] + out
                    temp-=1
                out = romans[5*r] + out
        return out
                
            
            
        