class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
#         start = 0
#         end = len(nums)-1
        
#         while start <= end:
#             middle = int(start + (end-start)/2)
#             if target == nums[middle]:
#                 return middle
#             elif target < nums[middle]:
#                 end = middle - 1
#             else:
#                 start = middle + 1
#         return -1
    
        i,j=0,len(nums)-1
        while(i<=j):
            mid=(i+j)//2
            if target < nums[mid]:
                j=mid-1
            elif target> nums[mid]:
                i=mid+1
            else:
                return mid
        return -1