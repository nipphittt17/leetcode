class Solution:
    
    first = 0
    sec = 1
     
    def fib(self, n: int) -> int:
       
        if n == 0 or n == 1:
            return n
        if n == 2:
            return self.first + self.sec  
        
        temp = self.first + self.sec
        self.first = self.sec
        self.sec = temp
        
        return(self.fib(n-1))
            
        
            
        