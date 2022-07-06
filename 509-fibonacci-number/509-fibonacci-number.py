class Solution:
    def fib(self, n: int) -> int:
        
        first = 0
        sec = 1
        
        if n == 0:
            return first

        out = 0
        n -= 2
        
        while(n > 0):
            temp = first + sec
            first = sec
            sec = temp
            n-=1
            
        return first + sec   
            
        