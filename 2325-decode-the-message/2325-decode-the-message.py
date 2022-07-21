class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decode = {}
        i = 0
        for k in key:
            if i == 26:
                break
            elif k != ' ' and k not in decode: 
                decode[k] = chr(97+i)
                i+=1
            
        output = ""
        
        for m in message:
            if m in decode:
                output+=decode[m]
            else:
                output+=' '
            
        return output
            
        