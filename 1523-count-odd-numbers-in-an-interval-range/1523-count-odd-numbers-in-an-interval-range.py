class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high - low + 1)%2 == 0: #one is even, another is odd
            return int((high - low +1)/2) 
        elif (high %2 == 0): #both is even
            return int((high-low)/2)
        else: #both is odd
            return int((high-low)/2 +1)
        
            
        