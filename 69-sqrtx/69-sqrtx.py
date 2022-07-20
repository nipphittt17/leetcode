class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        end = x
        
        while start <= end:
            
            mid = (start+end)//2
            result = mid*mid
            if result == x:
                return mid
            
            elif result > x:
                if (mid-1)*(mid-1) == x:
                    return mid-1
                elif (mid-1)*(mid-1) > x:
                    end = mid-1
                else: return mid-1  
                
            else:
                if (mid+1)*(mid+1) == x:
                    return mid+1
                elif (mid+1)*(mid+1) < x:
                    start = mid+1
                else: return mid
                
        return 0