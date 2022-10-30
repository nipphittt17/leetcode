class Solution:
    def isHappy(self, n: int) -> bool:
        passed = set()
        
        while (n not in passed):
            
            passed.add(n)
            
            sum = 0
 
            for char in str(n):
                sum += int(char) ** 2
            if sum == 1: return True
            n = sum

        return False
        