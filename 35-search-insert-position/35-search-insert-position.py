class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = 0
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target: return mid
            
            elif target < nums[mid]:
                if mid != 0 and nums[mid-1] == target: return mid-1
                else: right = mid-1
                    
            else:
                if mid!=len(nums)-1 and nums[mid+1] == target: return mid+1
                else: left = mid+1
                    
        if left>right: mid = left
        return mid
      