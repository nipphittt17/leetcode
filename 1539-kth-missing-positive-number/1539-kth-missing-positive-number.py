class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        missing = [0]
        for i in range(max(arr)):
            if i+1 not in arr:
                missing.append(i+1)

        left = 0
        right = len(missing)-1
        while left <= right:
            mid = (left+right)//2
            if mid == k:
                return missing[mid]
            elif mid < k: left = mid+1
            else: right = mid-1
        
        return max(arr) + k - len(missing) +1

            
            
        