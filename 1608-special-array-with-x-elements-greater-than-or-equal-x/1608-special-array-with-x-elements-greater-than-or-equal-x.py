class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums)
        
        while left <= right:
            mid = (left+right)//2
            
            count = 0
            for num in nums:
                if num >= mid: count+=1
            if mid == count:
                return mid
            elif mid < count:
                left = mid+1
            else:
                right = mid-1
                
        return -1
        