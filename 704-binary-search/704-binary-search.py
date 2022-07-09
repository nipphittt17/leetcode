class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        start,end = 0, len(nums)-1
        
        while start <= end:
            middle = start + (end-start)//2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
        return -1
    