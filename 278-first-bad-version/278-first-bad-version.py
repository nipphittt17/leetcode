# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while left <= right:
            mid = (left+right)//2
            if isBadVersion(mid) == True:
                if isBadVersion(mid-1) == False:
                    return mid
                else: right = mid-1
            else: left = mid+1
        
                
        