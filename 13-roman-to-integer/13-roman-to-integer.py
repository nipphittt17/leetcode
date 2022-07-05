class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M' : 1000,   
        }
        
        out = 0
        
        for i,x in enumerate(s):
            if i != 0:
                if x == 'V' or x == 'X':
                    if s[i-1] == 'I':
                        out -= 2*roman.get(s[i-1])
                elif x == 'L' or x == 'C':
                    if s[i-1] == 'X':
                        out -= 2*roman.get(s[i-1])
                elif x == 'D' or x == 'M':
                    if s[i-1] == 'C':
                        out -= 2*roman.get(s[i-1])
            out += roman.get(x)

        return out
            
        