class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        left = 0
        right = len(strX)-1
        
        while left < right:
            if strX[left] != strX[right]:
                return False
            left+=1
            right-=1
        
        return True