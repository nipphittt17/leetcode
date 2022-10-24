class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    
        # if(len(s) == 1 and s[0] != ' ') return 1
        i = len(s)-1
        m = 2
        while(s[i] == ' '):
            i = len(s)-m
            m+=1
        count = 0

        while s[i] != ' ' and i>=0:
            count+=1
            i-=1
        return count