class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        output = 0
        hasNeg = False
        for g in grid:
            left = 0
            right = len(g)-1
            
            while left <= right:
                mid = left+(right-left)//2
                if g[mid] < 0:
                    right = mid-1
                    hasNeg = True
                else:
                    left = mid+1
                    
            if hasNeg == False:
                output = 0
            
            else: output += len(g)-(right+1)
        return output