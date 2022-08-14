class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) < 2: return strs[0]
        
        output = ''
        index = 0
        for common in strs[0]:
            for s in strs[1:]:
                if index < len(s):
                    if s[index] != common:
                        return output
                    else: out = common
                else: return output
            output += out
            index += 1

        return output
            
        
            
        