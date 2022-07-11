class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = []
        
        for i,x in enumerate(nums):
            sum2 = 0 - x
            triplet = []
            
            left = i+1
            right = len(nums)-1
            
            while left<right:
                if nums[left] + nums[right] == sum2:
                    
                    triplet = [x,nums[left],nums[right]]
                    
                    if triplet not in triplets:
                        triplets.append(triplet)   
                        triplet = [x]
                    left+=1
                    right-=1
                elif nums[left] + nums[right] < sum2:
                    left+=1
                else:
                    right-=1
                
        return triplets