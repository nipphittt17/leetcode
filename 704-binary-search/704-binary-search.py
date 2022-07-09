class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        # start,end = 0, len(nums)-1
        
        # while start <= end:
        #     middle = (end+start)//2
        #     if target == nums[middle]:
        #         return middle
        #     elif target < nums[middle]:
        #         end = middle - 1
        #     else:
        #         start = middle + 1
        # return -1
    
        def binarySearch(nums, target, l, r):        
            while (r >= l):
                mid = (l+r)//2
                if (nums[mid] == target):
                    return mid
                elif (nums[mid] < target):
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
    
        return binarySearch(nums, target, 0, len(nums)-1)