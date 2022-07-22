class Solution:
    
    def arrangeCoins(self, n: int) -> int:

        left = 1
        right = n-1
        mid = left
        while left <= right:
            
            mid = (left+right)//2
            coin = mid * (mid+1) //2
            if coin == n: return mid
            elif coin < n:
                if (mid+1)*(mid+2)//2 > n:
                    return mid
                left = mid+1
            else:
                if (mid-1)*mid//2 < n:
                    return mid-1
                right = mid-1
        return mid
                
            
    
        
            