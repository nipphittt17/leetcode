class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        missing = []
        maxNum = max(arr)
        
        for i in range(maxNum+1):
            missing.append(i)
    
        for num in arr:
            missing.remove(num)
        
        length = len(missing)
        left = 0
        right = length-1
        while left <= right:
            mid = (left+right)//2
            if mid == k:
                return missing[mid]
            elif mid < k: left = mid+1
            else: right = mid-1
        
        return maxNum + k - length +1

            
            
        